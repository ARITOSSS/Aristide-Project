import unittest
from minesweeper import MinesweeperSolver  # Assurez-vous que le nom du fichier principal est correct

class TestMinesweeperSolver(unittest.TestCase):

    def setUp(self):
        """Initialize a new MinesweeperSolver for each test."""
        self.solver = MinesweeperSolver(8, 8, 10)  # Grid de 8x8 avec 10 bombes

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

if __name__ == '__main__':
    unittest.main()
