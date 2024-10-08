"""
This module contains the implementation of the Minesweeper solver using the
Double Set Single Point (DSSP) algorithm.
"""

import random
import time
from minesweeper import MinesweeperGame


class MinesweeperSolverDSSP:
    """
    Minesweeper Solver using Double Set Single Point (DSSP) algorithm.

    Attributes:
        game (MinesweeperGame): Instance of the MinesweeperGame to solve.
        s (set): Set of cells to be probed.
        q (set): Set of insecure cells.
        opener: First Move.
    """

    def __init__(self, game: MinesweeperGame):
        """
        Initialize the solver with a game instance and set default values.

        Args:
            game (MinesweeperGame): Instance of the Minesweeper game.
        """
        self.game = game
        self.opener = (self.select_corner_or_random())
        self.s = {self.opener}
        self.q = set()


    def select_corner_or_random(self):
        """
        Select a corner cell if available; otherwise, select a random unrevealed 
        and unflagged cell.

        Returns:
            tuple: The selected cell (row, col) or None if no valid cell exists.
        """

        corners = [
            (0, 0),
            (0, self.game.cols - 1),
            (self.game.rows - 1, 0),
            (self.game.rows - 1, self.game.cols - 1)
        ]

        # Return the first valid corner cell found
        for corner in corners:
            if corner not in self.game.revealed_cells and corner not in self.game.flags:
                return corner

        # If no free corner exists, select a random unrevealed cell
        unrevealed_cells = [
            (r, c) for r in range(self.game.rows)
            for c in range(self.game.cols)
            if (r, c) not in self.game.revealed_cells and (r, c) not in self.game.flags
        ]
        return random.choice(unrevealed_cells) if unrevealed_cells else None

    def is_all_free_neighbor(self, cell):
        """
        Check if a given cell is an "All Free Neighbor" (AFN), meaning that all
        neighboring cells that are not flagged are safe to explore.
        
        Args:
            cell (tuple): A tuple representing the coordinates (row, col) of the cell
                        in the Minesweeper grid to check.

        Returns:
            bool: Returns True if all unflagged neighboring cells are safe (i.e., all
                bombs have been flagged around this cell), False otherwise.
        """
        neighbors = self.game.get_neighbors(cell)
        bombs = self.game.count_adjacent_bombs(cell)
        flagged_neighbors = [n for n in neighbors if n in self.game.flags]
        count_flagged = len(flagged_neighbors)       

        return count_flagged == bombs

    def is_all_marked_neighbor(self, cell):
        """
        Check if a given cell is an "All Marked Neighbor" (AMN), meaning that all
        unmarked neighboring cells are mines.

        Args:
            cell (tuple): A tuple representing the coordinates (row, col) of the cell
                        in the Minesweeper grid to check.

        Returns:
            bool: Returns True if all unmarked neighboring cells around the given cell 
                are mines (i.e., the sum of flagged neighbors and unmarked cells equals
                the number of bombs around this cell). Returns False otherwise.
        """
        neighbors = self.game.get_neighbors(cell)
        unmarked_neighbors = [
            n for n in neighbors
            if n not in self.game.flags and n not in self.game.revealed_cells
        ]
        bombs = self.game.count_adjacent_bombs(cell)
        flagged_neighbors = [n for n in neighbors if n in self.game.flags]
        count_flagged = len(flagged_neighbors)

        return count_flagged + len(unmarked_neighbors) == bombs

    def step_solve(self, max_steps=None):
        """
        Solve the Minesweeper game with the sets s (certain cells) and q (potential mines).
        Using Double Set Single Point Algorithm.
        
        Args:
            max_steps (int, optional): Maximum number of steps to execute. If None, the solver 
                                    runs until the game is over.
        """
        index = 0
        while not self.game.game_over:
            index += 1
            if self.game.gui == True :
                print(f"Step {index}")

            if max_steps and index > max_steps:
                break

            if not self.s:
                x = self.select_corner_or_random()
                if x is not None:
                    self.s.add(x)

            if self.game.gui == True :
                print(" Set s : ",self.s)
            while self.s:
                x = self.s.pop()
                self.game.process_event(x)
                if self.game.gui == True:
                    time.sleep(0.2)
                    self.game.window.update()

                neighbors = self.game.get_neighbors(x)
                unmarked_neighbors = [
                    n for n in neighbors
                    if n not in self.game.flags and n not in self.game.revealed_cells
                ]

                if self.is_all_free_neighbor(x):
                    self.s.update(unmarked_neighbors)
                else:
                    self.q.add(x)

            to_remove_from_q = []
            if self.game.gui == True:
                print(" Set q : ",self.q)
            for q in list(self.q):
                neighbors = self.game.get_neighbors(q)
                unmarked_neighbors = [
                    n for n in neighbors
                    if n not in self.game.flags and n not in self.game.revealed_cells
                ]
                if self.is_all_marked_neighbor(q):
                    for y in unmarked_neighbors:
                        if y not in self.game.flags:
                            self.game.place_flag(y)
                    to_remove_from_q.append(q)

            for q in to_remove_from_q:
                self.q.discard(q)

            for q in list(self.q):
                neighbors = self.game.get_neighbors(q)
                unmarked_neighbors = [
                    n for n in neighbors
                    if n not in self.game.flags and n not in self.game.revealed_cells
                ]
                if self.is_all_free_neighbor(q):
                    self.s.update(unmarked_neighbors)
                    self.q.discard(q)

            if self.game.gui == True:
                time.sleep(1.5)
                self.game.window.update()
                print("-----------------------")




    def run_games(self, num_games: int , rows: int, cols: int, num_bombs: int):
        """
        Run multiple games and return the percentage of wins.

        Args:
            num_games (int): Number of games to run.

        Returns:
            float: Percentage of games won.
        """
        wins = 0
        iterations = 0
        for _ in range(num_games):
            game_instance = MinesweeperGame(rows, cols, num_bombs, gui=False)
            self.game = game_instance
            if self.opener not in self.game.bomb_locations:
                iterations += 1
                self.step_solve()
                if self.game.check_win():
                    wins += 1
        return wins / iterations * 100
    
if __name__ == "__main__":
    # Create a game instance (e.g., beginner difficulty)
    game = MinesweeperGame(16, 16, 40)



    # Start the solver
    solver = MinesweeperSolverDSSP(game)
    
    # Start the game and wait 2 seconds before the solver starts
    game.window.after(2000, solver.step_solve)
    game.start_game()

