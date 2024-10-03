from minesweeper import MinesweeperGame
from DSSP_solver import MinesweeperSolverDSSP
from NSP_solver import MinesweeperSolverNSP

if __name__ == "__main__":
    DSSP = MinesweeperSolverDSSP(MinesweeperGame(8, 8, 10, gui=False))
    NSP = MinesweeperSolverNSP(MinesweeperGame(8, 8, 10, gui=False))


    percentage_of_wins_DSSP = DSSP.run_games(1000)  # Lancer 50 parties

    percentage_of_wins_NSP = NSP.run_games(1000)  # Lancer 50 parties

    print(f"Pourcentage de victoires du DSSP: {percentage_of_wins_DSSP:.2f}%")
    print(f"Pourcentage de victoires du NSP: {percentage_of_wins_NSP:.2f}%")

