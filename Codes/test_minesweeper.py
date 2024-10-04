import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from minesweeper import MinesweeperGame

class TestMinesweeperGame(unittest.TestCase):
    def setUp(self):
        self.rows = 2
        self.cols = 2
        self.num_bombs = 2
        self.game = MinesweeperGame(self.rows, self.cols, self.num_bombs, gui=False)

    def test_generate_bomb_locations(self):
        bomb_locations = self.game.generate_bomb_locations(self.rows, self.cols, self.num_bombs)
        self.assertEqual(len(bomb_locations), self.num_bombs)
        self.assertTrue(all(0 <= loc[0] < self.rows and 0 <= loc[1] < self.cols for loc in bomb_locations))

    def test_count_adjacent_bombs(self):
        self.game.bomb_locations = {(0, 0), (0, 1)}
        self.assertEqual(self.game.count_adjacent_bombs((1, 0)), 2)  
        self.assertEqual(self.game.count_adjacent_bombs((1, 1)), 2)  

    def test_get_neighbors(self):
        neighbors = self.game.get_neighbors((1, 1))
        expected_neighbors = [
            (0, 0), (0, 1), (1, 0)
        ]
        self.assertEqual(sorted(neighbors), sorted(expected_neighbors))

    def test_reveal_cell(self):
        self.game.bomb_locations = {(1, 1)}
        self.game.reveal_cell((0, 0))
        self.assertIn((0, 0), self.game.revealed_cells)

    def test_place_flag(self):
        self.game.place_flag((0, 0))
        self.assertIn((0, 0), self.game.flags)
        self.game.place_flag((0, 0))
        self.assertNotIn((0, 0), self.game.flags)

    def test_check_win(self):
        self.game.bomb_locations = {(0, 1), (1, 1)}
        self.game.revealed_cells = {(1, 0), (0, 0)}  # Simulate revealing non-bomb cells
        self.assertTrue(self.game.check_win())

    def test_process_event_bomb(self):
        self.game.bomb_locations = {(1, 1)}
        self.game.process_event((1, 1))
        self.assertTrue(self.game.game_over)

    def test_process_event_win(self):
        self.game.bomb_locations = {(1, 1)}
        self.game.process_event((0, 0))
        self.game.process_event((0, 1))
        self.game.process_event((1, 0))
        self.assertTrue(self.game.check_win())


if __name__ == "__main__":
    unittest.main()
