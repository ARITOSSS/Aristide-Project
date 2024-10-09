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
        self.opener = self.select_random()
        self.s = set()
        self.q = set()



    def select_random(self):
        """
        Select a corner cell if available; otherwise, select a random unrevealed 
        and unflagged cell.

        Returns:
            tuple: The selected cell (row, col) or None if no valid cell exists.
        """

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
        self.s.add(self.opener)
        time.sleep(2)
        iterations = 0
        while not self.game.game_over:
            if not self.s:
                x = self.select_random()
                if x is not None:
                    self.s.add(x)

            if max_steps is not None and max_steps == 0:
                break

            if self.game.gui is True:
                iterations +=1
                print("Iteration: ", iterations)
                print("Set s: ", self.s)
            while self.s:
                x = self.s.pop()
                self.game.process_event(x)
                neighbors = self.game.get_neighbors(x)
                unmarked_neighbors = [
                    n for n in neighbors
                    if n not in self.game.flags and n not in self.game.revealed_cells
                ]

                if self.is_all_free_neighbor(x):
                    for y in unmarked_neighbors:
                        self.s.add(y)
                else:
                    self.q.add(x)

            if self.game.gui is True:
                print("Set q: ", self.q)
            for cell in list(self.q):
                neighbors = self.game.get_neighbors(cell)
                unmarked_neighbors = [
                    n for n in neighbors
                    if n not in self.game.flags and n not in self.game.revealed_cells
                ]
                if self.is_all_marked_neighbor(cell):
                    for y in unmarked_neighbors:
                        self.game.place_flag(y)
                    self.q.discard(cell)

            for cell in list(self.q):
                neighbors = self.game.get_neighbors(cell)
                unmarked_neighbors = [
                    n for n in neighbors
                    if n not in self.game.flags and n not in self.game.revealed_cells
                ]
                if self.is_all_free_neighbor(cell):
                    for y in unmarked_neighbors:
                        self.s.add(y)
                    self.q.discard(cell)
            if self.game.gui is True:
                time.sleep(2)
                self.game.window.update()

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
            if self.opener not in self.game.bomb_locations :
                iterations += 1
                self.step_solve()
                if self.game.check_win():
                    wins += 1
        return wins / iterations * 100
