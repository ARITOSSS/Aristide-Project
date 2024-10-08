import numpy as np
from tqdm import tqdm
from minesweeper import MinesweeperGame
from dssp_solver import MinesweeperSolverDSSP

def main():
    # Initialiser le solveur avec une configuration de jeu
    DSSP = MinesweeperSolverDSSP(MinesweeperGame(9, 9, 10, gui=False))

    wins_list_beginner = []  # Liste pour stocker les victoires
    wins_list_intermediate = []  # Liste pour stocker les victoires intermédiaires
    # Exécuter le nombre d'itérations spécifié avec une barre de progression
    for _ in tqdm(range(25), desc="Exécution des parties"):
        wins = DSSP.run_games(1000, 9, 9, 10)  # Lancer 1000 parties
        wins_list_beginner.append(wins)

    for _ in tqdm(range(25), desc="Exécution des parties"):
        wins = DSSP.run_games(1000, 16, 16, 40)  # Lancer 1000 parties
        wins_list_intermediate.append(wins)

    global_win_percentage = np.mean(wins_list_beginner)  # Calculer le pourcentage global de victoires
    print(f"Pourcentage de victoires pour chaque partie: {wins_list_beginner}")
    print(f"Pourcentage global de victoires du DSSP: {global_win_percentage:.2f}%")

    global_win_percentage_2 = np.mean(wins_list_intermediate)  # Calculer le pourcentage global de victoires
    print(f"Pourcentage de victoires pour chaque partie: {wins_list_intermediate}")
    print(f"Pourcentage global de victoires du DSSP: {global_win_percentage_2:.2f}%")

if __name__ == "__main__":
    main()
