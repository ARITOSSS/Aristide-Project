"""Unit tests for the MinesweeperSolverDSSP class."""
import unittest
from minesweeper import MinesweeperGame
from dssp_solver import MinesweeperSolverDSSP

class TestMinesweeperSolverDSSP(unittest.TestCase):
    """Unit tests for the MinesweeperSolverDSSP class."""

    def setUp(self):
        """Initialize a Minesweeper game instance for testing."""
        self.game = MinesweeperGame(5, 5, 4, False)  # A 5x5 grid with 4 bombs
        self.solver = MinesweeperSolverDSSP(self.game)

        # Set a known state of the grid
        self.game.revealed_cells = {(1, 1), (1, 2), (2, 1)}
        self.game.flags = {(0, 0), (1, 0)}

    def test_select_random(self):
        """Test random selection of an unrevealed and unflagged cell."""
        result = self.solver.select_random()

        # Verify the result is not a revealed or flagged cell
        self.assertNotIn(result, self.game.revealed_cells)
        self.assertNotIn(result, self.game.flags)

        # Simulate all cells revealed or flagged
        self.game.revealed_cells = {
            (r, c) for r in range(self.game.rows) for c in range(self.game.cols)
        }
        self.game.flags = set()

        # Check that the function returns None when no cells are available
        result = self.solver.select_random()
        self.assertIsNone(result)

        # Simulate some cells still available
        self.game.revealed_cells = {(0, 0), (1, 1)}
        self.game.flags = {(0, 1)}
        random_cell = self.solver.select_random()

        # Verify the chosen cell is neither revealed nor flagged
        self.assertNotIn(random_cell, self.game.revealed_cells)
        self.assertNotIn(random_cell, self.game.flags)

    def test_is_all_free_neighbor(self):
        """Test if a neighbor is "All Free Neighbor"."""
        cell = (0, 0)
        self.game.flags = {(1, 0)}
        self.game.bomb_locations = {(1, 0)}  # Example bomb
        self.assertTrue(self.solver.is_all_free_neighbor(cell))

    def test_is_all_marked_neighbor(self):
        """Test if a neighbor is "All Marked Neighbor"."""
        cell = (0, 0)
        self.game.revealed_cells = {(1, 1), (0, 1)}
        self.game.bomb_locations = {(1, 0)}
        self.assertTrue(self.solver.is_all_marked_neighbor(cell))

    def test_step_solve_win(self):
        """Test the solver's ability to win a game."""
        game = MinesweeperGame(5, 5, 4, False)
        game.bomb_locations = {(2, 3), (2, 1), (2, 4), (3, 3)}

        # Start the solver
        solver = MinesweeperSolverDSSP(game)
        solver.opener = (0, 0)
        solver.step_solve()

        # Check if the game is won
        self.assertTrue(game.check_win())

    def test_step_solve_limited_steps(self):
        """Test if the solver handles an empty set 's' correctly during execution
        by limiting steps."""
        # Create a new game for this test
        game = MinesweeperGame(5, 5, 4, gui=False)
        game.bomb_locations = {(2, 3)}

        # Instantiate a DSSP solver for this game
        solver = MinesweeperSolverDSSP(game)
        solver.s = set()

        # Limit the number of steps in step_solve to simulate an interruption
        solver.step_solve(max_steps=1)

        # Ensure set 's' is not empty after selecting a new cell
        self.assertNotEqual(
            len(solver.s), 0,
            "The set 's' should not be empty after selecting a new cell mid-execution."
        )

    def test_run_games(self):
        """Test the run_games method for win rate."""
        win_rate = self.solver.run_games(5, 5, 5, 5)
        # Check that the win rate is between 0 and 100
        self.assertTrue(0 <= win_rate <= 100)

if __name__ == "__main__":
    unittest.main()
