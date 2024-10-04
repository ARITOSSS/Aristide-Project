from minesweeper import MinesweeperGame
from nsp_solver import MinesweeperSolverNSP



if __name__ == "__main__":
    NSP = MinesweeperSolverNSP(MinesweeperGame(9, 9, 10, gui=False))

    percentage_of_wins_NSP = NSP.run_games(100)  # Lancer 50 parties
    print(f"Pourcentage de victoires du NSP: {percentage_of_wins_NSP:.2f}%")
