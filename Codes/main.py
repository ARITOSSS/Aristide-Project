""" Main file to run the Minesweeper game and the DSSP solver. """
from minesweeper import MinesweeperGame
from dssp_solver import MinesweeperSolverDSSP

def main() :
    """ Main function to run the Minesweeper game and the DSSP solver. """
    # Create a game instance (e.g., beginner difficulty)
    game = MinesweeperGame(9, 9, 10)
    # Start the solver
    solver = MinesweeperSolverDSSP(game)
    solver.opener = (0, 0)
    game.bomb_locations = {(7,7), (2,7), (0,3), (1,7), (4,5), (0,2), (3,6), (8,2), (1,3),(7,8)}
    # Start the game and wait 2 seconds before the solver starts
    game.window.after(2000, solver.step_solve)
    game.start_game()

if __name__ == "__main__":
    main()
