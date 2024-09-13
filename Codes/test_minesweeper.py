import unittest
from unittest.mock import patch, MagicMock
from minesweeper import MinesweeperGame

class TestMinesweeperGame(unittest.TestCase):

    def setUp(self):
        """Initialize a new MinesweeperSolver for each test."""
        self.solver = MinesweeperGame(8, 8, 10)

    def test_generate_bomb_locations(self):
        """Test the bomb locations are generated correctly."""
        first_click = (0, 0)
        bomb_locations = self.solver.generate_bomb_locations(8, 8, 10, first_click)
        self.assertEqual(len(bomb_locations), 10)
        self.assertNotIn(first_click, bomb_locations)

    def test_get_neighbors(self):
        """Test getting valid neighboring cells."""
        neighbors = self.solver.get_neighbors((1, 1))
        expected_neighbors = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 2),
            (2, 0), (2, 1), (2, 2)
        ]
        self.assertCountEqual(neighbors, expected_neighbors)

    def test_place_flag(self):
        """Test placing and removing flags."""
        cell = (3, 3)
        self.solver.place_flag(cell)
        self.assertIn(cell, self.solver.flags)
        self.solver.place_flag(cell)
        self.assertNotIn(cell, self.solver.flags)

    def test_reveal_cell(self):
        """Test revealing a cell and its adjacent cells."""
        self.solver.bomb_locations = [(1, 1)]
        self.solver.reveal_cell((0, 0))
        self.assertIn((0, 0), self.solver.revealed_cells)
        self.assertNotIn((1, 1), self.solver.revealed_cells)

    @patch('tkinter.messagebox.showinfo')
    def test_process_event_loss(self, mock_showinfo):
        """Test losing the game when clicking on a bomb."""
        self.solver.process_event((0, 1)) 

        self.solver.bomb_locations = [(0, 0)]

        self.solver.process_event((0, 0))

        self.assertTrue(self.solver.game_over)
        mock_showinfo.assert_called_once_with("Lost", "Bomb! You lost.")


    def test_check_win(self):
        """Test the check win condition."""
        self.solver.bomb_locations = [(0, 0)]
        self.solver.revealed_cells = {(r, c) for r in range(8) for c in range(8) if (r, c) != (0, 0)}
        self.assertTrue(self.solver.check_win())

    def test_reveal_initial_safe_zone(self):
        """Test the initial safe zone is revealed correctly after the first click."""
        self.solver.bomb_locations = [(2, 2), (3, 3), (4, 4)]
        self.solver.reveal_initial_safe_zone((0, 0))
        # Check that the initial cell and some neighbors are revealed
        self.assertIn((0, 0), self.solver.revealed_cells)
        self.assertGreaterEqual(len(self.solver.revealed_cells), 1)  # At least the clicked cell should be revealed

    def test_count_adjacent_bombs(self):
        """Test counting adjacent bombs correctly."""
        self.solver.bomb_locations = [(1, 1), (2, 2)]
        count = self.solver.count_adjacent_bombs((1, 2))
        self.assertEqual(count, 2)

if __name__ == '__main__':
    unittest.main()
