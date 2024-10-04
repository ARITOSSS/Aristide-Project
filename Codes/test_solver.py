import unittest
from unittest.mock import MagicMock
from nsp_solver import MinesweeperSolverNSP
from minesweeper import MinesweeperGame

class TestMinesweeperSolverNSP(unittest.TestCase):
    def setUp(self):
        """Set up a Minesweeper game instance for testing."""
        self.game = MagicMock(spec=MinesweeperGame)
        self.game.rows = 9
        self.game.cols = 9
        self.game.bomb_locations = {(1, 1), (2, 2)}  # Example bomb locations
        self.game.revealed_cells = set()
        self.game.flags = set()
        self.game.count_adjacent_bombs.return_value = 2  # Example count of bombs around a cell
        self.game.get_neighbors.return_value = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 1)]  # Example neighbors

        self.solver = MinesweeperSolverNSP(self.game)

    def test_select_corner_or_random(self):
        """Test selecting a corner or a random cell."""
        # Setup unrevealed and unflagged cells
        self.game.revealed_cells = {(0, 0), (0, 1)}
        self.game.flags = {(1, 1)}
        
        # Select a corner or random cell
        selected_cell = self.solver.select_corner_or_random()
        self.assertIn(selected_cell, [(0, 0), (0, self.game.cols - 1),
                                       (self.game.rows - 1, 0), (self.game.rows - 1, self.game.cols - 1), (1, 0), (1, 1)])
        
    def test_step_solve(self):
        """Test the step_solve functionality."""
        self.solver.s = {(0, 0)}  # Set the initial cell to probe
        self.game.process_event = MagicMock()
        
        result = self.solver.step_solve()
        
        # Check if the process_event was called
        self.game.process_event.assert_called_once_with((0, 0))
        
        # Check if the method returns "Failure" when hitting a bomb
        self.game.process_event.return_value = True  # Simulate that we hit a bomb
        self.assertEqual(self.solver.step_solve(), "Failure")

    def test_run_games(self):
        """Test the run_games method for multiple game runs."""
        self.solver.step_solve = MagicMock()  # Mock the step_solve method
        self.solver.game.check_win.return_value = True  # Mock winning condition

        wins_percentage = self.solver.run_games(10)  # Run 10 games
        self.assertEqual(wins_percentage, 100.0)  # All games won

        # Check that step_solve was called 10 times
        self.assertEqual(self.solver.step_solve.call_count, 10)

if __name__ == "__main__":
    unittest.main()
