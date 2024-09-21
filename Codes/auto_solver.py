from minesweeper import MinesweeperGame
import random

class MinesweeperSolverNSSP:
    """
    Minesweeper Solver using Naive Single Point (NSSP) algorithm.
    """

    def __init__(self, game: MinesweeperGame):
        """
        Initialize the solver with an instance of the MinesweeperGame.

        Args:
            game (MinesweeperGame): The instance of the game to solve.
        """
        self.game = game
        self.S = set()  # Set for cells to probe
        self.delay = 1000  # Delay between steps in milliseconds (1 second)

    def isAllFreeNeighbor(self, cell):
        for x in self.game.get_neighbors(cell):
            if x not in self.game.flags and x not in self.game.revealed_cells:
                return False
        return True


    def isAllMarkedNeighbor(self, cell):
        adjacent_bombs = self.game.count_adjacent_bombs(cell)
        marked_count = sum(1 for x in self.game.get_neighbors(cell) if x in self.game.flags)
        return marked_count == adjacent_bombs


    def step_solve(self):
        print("Début de l'étape de résolution")
        
        if self.game.game_over:
            print("Jeu terminé")
            return

        # Initialiser avec la première cellule si S est vide
        if not self.S :
            unopened_cells = [
                (r, c) for r in range(self.game.grid_size[0])
                for c in range(self.game.grid_size[1])
                if (r, c) not in self.game.revealed_cells and (r, c) not in self.game.flags
            ]
            
            if unopened_cells:
                opener = random.choice(unopened_cells)
                self.S.add(opener)
                print(f"Début avec {opener}")

        new_flags = set()
        new_safe_cells = set()
        
        # Parcourir toutes les cellules déjà révélées
        for cell in self.game.revealed_cells:
            neighbors = self.game.get_neighbors(cell)
            unmarked_neighbors = [n for n in neighbors if n not in self.game.revealed_cells and n not in self.game.flags]
            flagged_neighbors = [n for n in neighbors if n in self.game.flags]

            adjacent_bombs = self.game.count_adjacent_bombs(cell)

            # Si le nombre de drapeaux autour de la cellule révélée est égal au nombre d'adjacents, toutes les autres sont sûres
            if len(flagged_neighbors) == adjacent_bombs:
                for neighbor in unmarked_neighbors:
                    if neighbor not in self.S and neighbor not in new_safe_cells:
                        new_safe_cells.add(neighbor)
            
            # Si le nombre de voisins non marqués est égal au nombre d'adjacents restants, placer un drapeau
            if len(unmarked_neighbors) == adjacent_bombs - len(flagged_neighbors):
                for neighbor in unmarked_neighbors:
                    if neighbor not in self.game.flags and neighbor not in new_flags:
                        new_flags.add(neighbor)

        # Placer les nouveaux drapeaux
        for cell in new_flags:
            self.game.place_flag(cell)
            print(f"Drapeau placé sur: {cell}")

        # Explorer les nouvelles cellules sûres
        for cell in new_safe_cells:
            self.S.add(cell)

        if new_safe_cells:
            print(f"Cellules sûres ajoutées à explorer: {new_safe_cells}")
        else:
            print("Aucune nouvelle cellule sûre trouvée.")
               
        # Traiter toutes les cellules dans S (celles à explorer)
        for x in list(self.S):
            if x not in self.game.flags :
                self.game.process_event(x)
                if x in self.game.bomb_locations:
                    print("Bombe trouvée à:", x)
                    return  # Arrêter si on touche une bombe
                self.S.remove(x)
                print(f"Cellule explorée: {x}")

        # Relancer la boucle après un délai
        self.game.window.after(self.delay, self.step_solve)



if __name__ == "__main__":
    # Create a game instance (e.g., beginner difficulty)
    game = MinesweeperGame(8, 8, 10)

    # Start the solver
    solver = MinesweeperSolverNSSP(game)

    # Start the game and wait 2 seconds before the solver starts
    game.window.after(2000, solver.step_solve)
    game.start_game()
