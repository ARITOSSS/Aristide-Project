"""Unit tests for the Minesweeper game."""
import unittest
from minesweeper import MinesweeperGame

class TestMinesweeperGame(unittest.TestCase):
    """Unit test for the MinesweeperGame class."""

    def setUp(self):
        """Set up a Minesweeper game instance for testing."""
        self.rows = 2
        self.cols = 2
        self.num_bombs = 2
        self.game = MinesweeperGame(self.rows, self.cols, self.num_bombs, gui=False)

    def test_generate_bomb_locations(self):
        """Test that bomb locations are generated correctly."""
        # Generate bomb
        bomb_locations = self.game.generate_bomb_locations(self.rows, self.cols, self.num_bombs)
        # Check that the number of bomb locations is correct
        self.assertEqual(len(bomb_locations), self.num_bombs)
        # Check that all bomb locations are within the grid
        self.assertTrue(all(0 <= loc[0] < self.rows
                        and 0 <= loc[1] < self.cols for loc in bomb_locations))

    def test_count_adjacent_bombs(self):
        """Test the counting of adjacent bombs."""
        self.game.bomb_locations = {(0, 0), (0, 1)}
        self.assertEqual(self.game.count_adjacent_bombs((1, 0)), 2)  # Check for bombs around (1, 0)
        self.assertEqual(self.game.count_adjacent_bombs((1, 1)), 2)  # Check for bombs around (1, 1)

    def test_get_neighbors(self):
        """Test that the neighbors of a cell are correctly identified."""
        neighbors = self.game.get_neighbors((1, 1))
        expected_neighbors = [
            (0, 0), (0, 1), (1, 0)
        ]
        self.assertEqual(sorted(neighbors), sorted(expected_neighbors))

    def test_reveal_cell(self):
        """Test revealing a cell."""
        self.game.bomb_locations = {(1, 1)}
        self.game.reveal_cell((0, 0))
        self.assertIn((0, 0), self.game.revealed_cells)
        temp = self.game.reveal_cell((0, 0))
        self.assertTrue(temp== None)

    def test_place_flag(self):
        """Test placing and removing flags on cells."""
        self.game.place_flag((0, 0))
        self.assertIn((0, 0), self.game.flags)  # Flag should be placed
        self.game.place_flag((0, 0))
        self.assertNotIn((0, 0), self.game.flags)  # Flag should be removed

    def test_check_win(self):
        """Test winning condition in the game."""
        self.game.bomb_locations = {(0, 1), (1, 1)}
        self.game.revealed_cells = {(1, 0), (0, 0)}  # Simulate revealing non-bomb cells
        self.assertTrue(self.game.check_win())

    def test_process_event_bomb(self):
        """Test event processing when a bomb is triggered."""
        self.game.bomb_locations = {(1, 1)}
        self.game.process_event((1, 1))
        self.assertTrue(self.game.game_over)  # Game should be over

    def test_process_event_win(self):
        """Test event processing when the player wins."""
        self.game.bomb_locations = {(1, 1)}
        # Revealing all non-bomb cells
        self.game.process_event((0, 0))  
        self.game.process_event((0, 1))  
        self.game.process_event((1, 0))  
        self.assertTrue(self.game.check_win())  # Check if the win condition is met



if __name__ == "__main__":
    unittest.main()
