""" Module to calculate some statistics about the DSSP algorithm in Minesweeper. """
import numpy as np
import matplotlib.pyplot as plt
from minesweeper import MinesweeperGame
from dssp_solver import MinesweeperSolverDSSP

def main():
    """ Main function to calculate the win percentage of the DSSP algorithm in Minesweeper. """
    dssp = MinesweeperSolverDSSP(MinesweeperGame(9, 9, 10, gui=False))

    # Lists to store win percentages for each difficulty level
    wins_list_beginner = []
    wins_list_intermediate = []
    wins_list_expert = []

    # Open a markdown file to store results
    with open("Testing Document.md", "w", encoding="utf-8") as f:
        f.write("### DSSP Results: Starting with a Random Cell\n")

        # Run 10,000 games for each difficulty level
        for _ in range(10):  # Augmenter les itérations
            wins = dssp.run_games(1000, 9, 9, 10)  # Beginner level
            wins_list_beginner.append(wins)

        for _ in range(10):
            wins = dssp.run_games(1000, 16, 16, 40)  # Intermediate level
            wins_list_intermediate.append(wins)

        for _ in range(10):
            wins = dssp.run_games(1000, 16, 30, 99)  # Expert level
            wins_list_expert.append(wins)

        # Write the results to the markdown file
        global_win_percentage = np.mean(wins_list_beginner)
        f.write("#### Beginner Level\n")
        f.write(f"- Win percentage for each batch: {wins_list_beginner}\n")
        f.write(f"- Global win percentage of DSSP: {global_win_percentage:.2f}%\n\n")

        global_win_percentage_2 = np.mean(wins_list_intermediate)
        f.write("#### Intermediate Level\n")
        f.write(f"- Win percentage for each batch: {wins_list_intermediate}\n")
        f.write(f"- Global win percentage of DSSP: {global_win_percentage_2:.2f}%\n\n")

        global_win_percentage_3 = np.mean(wins_list_expert)
        f.write("#### Expert Level\n")
        f.write(f"- Win percentage for each batch: {wins_list_expert}\n")
        f.write(f"- Global win percentage of DSSP: {global_win_percentage_3:.2f}%\n")
        f.write("\n---\n")


def main2():
    """ Main function to calculate the win percentage of the DSSP algorithm in Minesweeper. """
    dssp = MinesweeperSolverDSSP(MinesweeperGame(9, 9, 10, gui=False))
    dssp.opener = (0, 0)

    # Lists to store win percentages for each difficulty level
    wins_list_beginner = []
    wins_list_intermediate = []
    wins_list_expert = []

    # Open a markdown file to store results
    with open("Testing_Document.md", "a", encoding="utf-8") as f:  # Use 'a' to append to the file
        f.write("### DSSP Results: Starting with a Corner Cell\n")

        # Run 10,000 games for each difficulty level
        for _ in range(10):  # Augmenter les itérations
            wins = dssp.run_games(1000, 9, 9, 10)  # Beginner level
            wins_list_beginner.append(wins)

        for _ in range(10):
            wins = dssp.run_games(1000, 16, 16, 40)  # Intermediate level
            wins_list_intermediate.append(wins)

        for _ in range(10):
            wins = dssp.run_games(1000, 16, 30, 99)  # Expert level
            wins_list_expert.append(wins)

        # Write the results to the markdown file
        global_win_percentage = np.mean(wins_list_beginner)
        f.write("#### Beginner Level\n")
        f.write(f"- Win percentage for each batch: {wins_list_beginner}\n")
        f.write(f"- Global win percentage of DSSP: {global_win_percentage:.2f}%\n\n")

        global_win_percentage_2 = np.mean(wins_list_intermediate)
        f.write("#### Intermediate Level\n")
        f.write(f"- Win percentage for each batch: {wins_list_intermediate}\n")
        f.write(f"- Global win percentage of DSSP: {global_win_percentage_2:.2f}%\n\n")

        global_win_percentage_3 = np.mean(wins_list_expert)
        f.write("#### Expert Level\n")
        f.write(f"- Win percentage for each batch: {wins_list_expert}\n")
        f.write(f"- Global win percentage of DSSP: {global_win_percentage_3:.2f}%\n")
        f.write("\n---\n")


def main3():
    """ Main function to run the simulations and plot the results. """
    dssp = MinesweeperSolverDSSP(MinesweeperGame(9, 9, 10, gui=False))
    wins_list_density = []
    mine_densities = []

    with open("Testing_Document.md", "a", encoding="utf-8") as f:
        f.write("### Win Percentage vs. Mine Density on a 9x9 grid\n")

        for mines in range(0, 33, 5):  # Increase the number of mines by steps of 5, up to 32 mines
            win_rate = dssp.run_games(1000, 9, 9, mines)
            wins_list_density.append(win_rate)
            density = mines / (9 * 9)
            mine_densities.append(density)

            f.write(f"- Mine Density: {density:.2f}, Win Percentage: {win_rate:.2f}%\n")

    # Plot the results as before
    plt.figure(figsize=(8, 6))
    plt.plot(mine_densities, wins_list_density, marker='s',
             linestyle='-', color='g', label='DSSP', markersize=7)
    plt.xlabel('Mine Density', fontsize=12)
    plt.ylabel('Win Percentage', fontsize=12)
    plt.title('Win Percent vs. Mine Density with fixed Board Size (81 squares)', fontsize=14)
    plt.grid(True)
    plt.xlim(0, 0.4)
    plt.ylim(0, 100)
    plt.legend(loc='upper right')

    # Save the plot in the Image directory using a relative path
    plt.savefig("./Image/mine_density_vs_win_percentage.png")

    # Include the plot in the markdown file
    with open("Testing_Document.md", "a", encoding="utf-8") as f:
        f.write("![Mine Density vs Win Percentage](./Codes/Images/mine_density_vs_win_percentage.png)\n")

#Uncomment the following lines to run the functions
# if __name__ == "__main__":
#    main()
#   main2()
#    main3()
