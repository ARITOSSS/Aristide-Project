import unittest
from unittest.mock import MagicMock, patch
from Codes.NSP_solver import MinesweeperSolverNSSP
from minesweeper import MinesweeperGame

class TestMinesweeperSolverNSSP(unittest.TestCase):
    def setUp(self):
        """
        Set up a basic Minesweeper game and solver for testing.
        """
        self.rows, self.cols, self.num_bombs = 8, 8, 10
        self.game = MinesweeperGame(self.rows, self.cols, self.num_bombs)
        self.solver = MinesweeperSolverNSSP(self.game)


    @patch('auto_solver.MinesweeperSolverNSSP.step_solve')
    def test_step_solve_called(self, mock_step_solve):
        """
        Test if step_solve is correctly called after first click.
        """
        self.solver.first_click = MagicMock()
        self.solver.step_solve()

        mock_step_solve.assert_called()

    def test_first_click(self):
        """
        Test if the solver correctly makes the first click.
        """
        self.game.reveal_initial_safe_zone = MagicMock()
        self.solver.first_click()

        self.game.reveal_initial_safe_zone.assert_called_once()

    def test_action(self):
        """
        Test the action() function for placing flags and revealing safe cells.
        """
        # Mock functions that modify the game's internal state
        self.game.place_flag = MagicMock()
        self.game.process_event = MagicMock()

        new_flags = {(1, 1), (2, 2)}
        new_safe_cells = {(3, 3), (4, 4)}

        # Execute the action
        self.solver.action(new_flags, new_safe_cells)

        # Assert flags were placed
        self.game.place_flag.assert_any_call((1, 1))
        self.game.place_flag.assert_any_call((2, 2))

        # Assert safe cells were explored
        self.game.process_event.assert_any_call((3, 3))
        self.game.process_event.assert_any_call((4, 4))



    def test_no_action_possible(self):
        """
        Test if the solver correctly handles cases where no action is possible.
        """
        self.solver.first_click = MagicMock()
        
        # Run step_solve with no possible actions
        self.solver.step_solve()

        # Check that first_click was called
        self.solver.first_click.assert_called_once()


    def test_is_all_marked_neighbors_true(self):
        # Simulate revealed and flagged neighbors
        self.game.flags = {(0, 1), (1, 0), (1, 1)}  # Set some neighbors as flagged
        self.solver.game.revealed_cells = {(0, 0)}  # Ensure the center cell is revealed
        result = self.solver.is_all_marked_neighbors((0, 0))
        self.assertTrue(result)

    def test_is_all_marked_neighbors_false(self):
        """
        Test if is_all_marked_neighbors returns False when not all neighbors are flagged or revealed.
        """
        self.game.revealed_cells = {(2, 2)}
        self.game.flags = {(1, 1)}
        
        result = self.solver.is_all_marked_neighbors((2, 2))
        self.assertFalse(result)

    def test_action_places_flags_correctly(self):
        """
        Test if action places flags on the correct cells.
        """
        # Mock the game's place_flag method
        self.game.place_flag = MagicMock()

        new_flags = {(2, 2), (3, 3)}
        self.solver.action(new_flags, set())

        # Check that place_flag was called for each flag
        self.game.place_flag.assert_any_call((2, 2))
        self.game.place_flag.assert_any_call((3, 3))

    def test_action_processes_safe_cells_correctly(self):
        """
        Test if action explores safe cells correctly.
        """
        # Mock the game's process_event method
        self.game.process_event = MagicMock()

        new_safe_cells = {(2, 2), (3, 3)}
        self.solver.action(set(), new_safe_cells)

        # Check that process_event was called for each safe cell
        self.game.process_event.assert_any_call((2, 2))
        self.game.process_event.assert_any_call((3, 3))



if __name__ == '__main__':
    unittest.main()
