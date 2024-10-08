import unittest
from minesweeper import MinesweeperGame
from dssp_solver import MinesweeperSolverDSSP  # Remplacez par le chemin correct

class TestMinesweeperSolverDSSP(unittest.TestCase):

    def setUp(self):
        # Crée une instance de MinesweeperGame avec un état fixe
        self.game = MinesweeperGame(5, 5, 4,False)  # Par exemple, une grille 5x5 avec 5 bombes
        self.solver = MinesweeperSolverDSSP(self.game)

        # Configurer un état connu de la grille
        # Marquer certaines cellules comme révélées et d'autres comme des drapeaux
        self.game.revealed_cells = {(1, 1), (1, 2), (2, 1)}
        self.game.flags = {(0, 0), (1, 0)}

    def test_select_corner_or_random(self):
        # Teste la sélection d'un coin ou d'une cellule aléatoire
        result = self.solver.select_corner_or_random()
        # Les coins sont (0,0), (0,4), (4,0), (4,4)
        expected_corners = {(0, 0), (0, 4), (4, 0), (4, 4)}
        
        # Vérifie que le résultat est soit un coin non révélé, soit une cellule aléatoire
        self.assertIn(result, expected_corners)
        # Vérifie qu'il n'a pas été révélé ni marqué
        self.assertNotIn(result, self.game.revealed_cells)
        self.assertNotIn(result, self.game.flags)

        self.game.revealed_cells = {(0, 0), (0, 4), (4, 0), (4, 4)}
        random_cell = self.solver.select_corner_or_random()
        self.assertTrue(random_cell not in expected_corners)

    def test_is_all_free_neighbor(self):
        # Teste si un voisin est "All Free Neighbor"
        cell = (0, 0)
        # Place les drapeaux et compte les bombes
        self.game.flags = {(1, 0)}
        self.game.bomb_locations = {(1, 0)}  # Exemples de bombes
        self.assertTrue(self.solver.is_all_free_neighbor(cell))

    def test_is_all_marked_neighbor(self):
        # Teste si un voisin est "All Marked Neighbor"
        cell = (0,0)
        self.game_flags = {}
        self.game.revealed_cells = {(1,1),(0,1)}
        self.game.bomb_locations = {(1, 0)}
        self.assertTrue(self.solver.is_all_marked_neighbor(cell))

    
    def test_step_solve_win(self):
        """
        Test the solver's ability to win a game.
        """
        game = MinesweeperGame(5, 5, 4,False)

        game.bomb_locations = {(2, 3), (2, 1), (2, 4), (3, 3)}


        # Start the solver
        solver = MinesweeperSolverDSSP(game)
        
        solver.step_solve()

        print(solver.s)

        self.assertTrue(game.check_win())
    
    def test_step_solve_limited_steps(self):
            """
            Test if the solver correctly handles an empty set 's' during execution by limiting steps.
            Covers lines 121-123, 127.
            """
            # Crée une nouvelle partie pour ce test
            game = MinesweeperGame(5, 5, 4, gui=True)
            game.bomb_locations = {(2, 3)}

            # Instancier un solver DSSP pour cette partie
            solver = MinesweeperSolverDSSP(game)

            # Vider l'ensemble 's' pour simuler une situation intermédiaire
            solver.s.clear()

            # Limiter le nombre de pas dans step_solve à 3 pour simuler une interruption
            solver.step_solve(max_steps=1)

            # Vérifier que l'ensemble 's' n'est plus vide après sélection d'une nouvelle cellule
            self.assertNotEqual(len(solver.s), 0, "The set 's' should not be empty after selecting a new cell in mid-execution.")






if __name__ == "__main__":
    unittest.main()
