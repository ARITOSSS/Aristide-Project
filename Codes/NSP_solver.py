"""
This module contains the implementation of the Minesweeper solver using the
Naive Single Point (NSP) algorithm.
"""

import random
import time
from minesweeper import MinesweeperGame

class MinesweeperSolverNSP:
    """
    Minesweeper Solver using Naive Single Point (NSP) algorithm.

    Attributes:
        game (MinesweeperGame): Instance of the MinesweeperGame to solve.
        s (set): Set of cells to be probed.
    """

    def __init__(self, game: MinesweeperGame):
        """
        Initialize the solver with a game instance and set default values.

        Args:
            game (MinesweeperGame): Instance of the Minesweeper game.
        """
        self.game = game
        self.s = set()  # Set for cells to probe
        self.delay = 2000  # Delay in milliseconds

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

    def step_solve(self):
        """
        Perform a step of solving the Minesweeper game.
        Using Naive Single Point Algorithm
        """
        while not self.game.game_over:
            # If set s is empty, select another cell
            if not self.s:
                x = self.select_corner_or_random()
                self.s.add(x)

            new_cells = set()  # To track newly discovered cells
            for x in list(self.s):
                self.game.process_event(x)  # Process the current cell

                if x in self.game.bomb_locations:
                    return "Failure"  # The cell clicked was a bomb

                # Gather information about the neighbors of the revealed cell
                neighbors = self.game.get_neighbors(x)
                unmarked_neighbors = [
                    n for n in neighbors
                    if n not in self.game.flags and n not in self.game.revealed_cells
                ]
                bombs = self.game.count_adjacent_bombs(x)
                flagged_neighbors = [n for n in neighbors if n in self.game.flags]
                count_flagged = len(flagged_neighbors)

                # If the number of bombs matches the number of flagged neighbors,
                # add unmarked neighbors to set s
                if bombs == count_flagged:
                    self.s.update(unmarked_neighbors)
                    new_cells.update(unmarked_neighbors)  # Track new cells discovered

                # If the count of flagged neighbors and unmarked neighbors equals bombs,
                # place flags on unmarked neighbors
                if count_flagged + len(unmarked_neighbors) == bombs:
                    for y in unmarked_neighbors:
                        if y not in self.game.flags:
                            self.game.place_flag(y)
            time.sleep(1)
            self.game.window.update()

            # Schedule the next step if the game is not over and new cells were found
            if not new_cells:
                x = self.select_corner_or_random()
                self.s.add(x)


    def run_games(self, num_games: int):
        """
        Run multiple games and return the percentage of wins.

        Args:
            num_games (int): Number of games to run.

        Returns:
            float: Percentage of games won.
        """
        wins = 0
        for _ in range(num_games):
            game_instance = MinesweeperGame(9, 9, 10, gui=False)  # Set gui to False
            self.game = game_instance
            self.step_solve()
            if self.game.check_win():
                wins += 1  # Increment win count if the game is won
        return wins / num_games * 100  # Calculate and return the win percentage

if __name__ == "__main__":
    # Create a game instance (e.g., beginner difficulty)
    game = MinesweeperGame(9, 9, 10)

    # Start the solver
    solver = MinesweeperSolverNSP(game)

    # Start the game and wait 2 seconds before the solver starts
    game.window.after(2000, solver.step_solve)
    game.start_game()
