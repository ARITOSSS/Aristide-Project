import random
from minesweeper import MinesweeperGame  

class MinesweeperSolverDSSP:
    """
    Minesweeper Solver using Naive Single Point (NSSP) algorithm.
    
    Attributes:
        game (MinesweeperGame): Instance of the MinesweeperGame to solve.
        S (set): Set of cells to be probed.
    """

    def __init__(self, game: MinesweeperGame):
        """
        Initialize the solver with a game instance and set default values.

        Args:
            game (MinesweeperGame): Instance of the Minesweeper game.
        """
        self.game = game
        self.s = set()  # Set for cells to probe
        self.q = set()

    def is_all_marked_neighbors(self, cell):
        """
        Check if all neighboring cells of the given cell are flagged or revealed.

        Args:
            cell (tuple): The cell (row, col) to check.

        Returns:
            bool: True if all neighboring cells are flagged or revealed, False otherwise.
        """
        for neighbor in self.game.get_neighbors(cell):
            if neighbor not in self.game.flags and neighbor not in self.game.revealed_cells:
                return False
        return True

    def first_click(self):
        """
        Handle the first click by probing the center cell of the grid.

        Returns:
            None
        """
        center_cell = (self.game.grid_size[0] // 2, self.game.grid_size[1] // 2)
        # Ensure the center cell is unopened
        if center_cell not in self.game.revealed_cells and center_cell not in self.game.flags:
            self.game.process_event(center_cell)

        # Start the solving process after the first click
        self.step_solve()

    def step_solve(self):
        """
        Perform each step of the solving process, 
        analyzing the current state and taking appropriate actions.

        Returns:
            None
        """
        new_flags = set()
        new_safe_cells = set()
        real_revealed_cells = set()

        # Analyze revealed cells that are not fully processed
        for cell in self.game.revealed_cells:
            if self.game.count_adjacent_bombs(cell) != 0 and not self.is_all_marked_neighbors(cell):
                real_revealed_cells.add(cell)

        # Process each relevant revealed cell
        for cell in real_revealed_cells:
            neighbors = self.game.get_neighbors(cell)
            unmarked_neighbors = [n for n in neighbors if n not in self.game.revealed_cells
            and n not in self.game.flags]
            flagged_neighbors = [n for n in neighbors if n in self.game.flags]

            adjacent_bombs = self.game.count_adjacent_bombs(cell)

            # If number of flagged neighbors equals the number of adjacent bombs, the rest are safe
            if len(flagged_neighbors) == adjacent_bombs:
                for neighbor in unmarked_neighbors:
                    if neighbor not in new_safe_cells:
                        new_safe_cells.add(neighbor)

            # If the number of unmarked neighbors equals the remaining bombs, mark them as bombs
            if len(unmarked_neighbors) == adjacent_bombs - len(flagged_neighbors):
                for neighbor in unmarked_neighbors:
                    if neighbor not in self.game.flags and neighbor not in new_flags:
                        new_flags.add(neighbor)

            else :
                self.q.add(cell)

        # Perform the actions determined by the analysis
        self.action(new_flags, new_safe_cells)

        to_remove = set()
        for cell in list(self.q):
            neighbors = self.game.get_neighbors(cell)
            unmarked_neighbors = [n for n in neighbors if n not in self.game.revealed_cells and n not in self.game.flags]
            flagged_neighbors = [n for n in neighbors if n in self.game.flags]
            adjacent_bombs = self.game.count_adjacent_bombs(cell)

            if len(flagged_neighbors) == adjacent_bombs:
                for neighbor in unmarked_neighbors:
                    if neighbor not in new_safe_cells:
                        new_safe_cells.add(neighbor)
                        # Schedule removal
                        to_remove.add(cell)

            if len(unmarked_neighbors) == adjacent_bombs - len(flagged_neighbors):
                for neighbor in unmarked_neighbors:
                    if neighbor not in self.game.flags and neighbor not in new_flags:
                        new_flags.add(neighbor)
                        # Schedule removal
                        to_remove.add(cell)

        # After processing, remove scheduled cells
        self.q.difference_update(to_remove)



        # If no new flags or safe cells, click a random unopened cell
        if not new_flags and not new_safe_cells and not self.s and not self.game.game_over:
            unopened_cells = [
                (r, c) for r in range(self.game.grid_size[0])
                for c in range(self.game.grid_size[1])
                if (r, c) not in self.game.revealed_cells and (r, c) not in self.game.flags
            ]
            # Random click on an unopened cell
            if unopened_cells:
                random_cell = random.choice(unopened_cells)
                self.game.process_event(random_cell)

        if not self.game.game_over:
            self.step_solve()  # Continue solving until the game is over

    def action(self, new_flags, new_safe_cells):
        """
        Perform the actions determined by the analysis.
        
        Args:
            new_flags (set): Set of new flags to place.
            new_safe_cells (set): Set of new safe cells to explore.
            
            Returns:
                None
        """
        # Place the new flags
        for cell in new_flags:
            self.game.place_flag(cell)

        # Explore new safe cells
        for cell in new_safe_cells:
            self.s.add(cell)

        # Process all cells in S (those marked for exploration)
        for x in list(self.s):
            if x not in self.game.flags:
                self.game.process_event(x)
                self.s.remove(x)

    def run_games(self, num_games: int):
        """
        Run multiple games and return the percentage of wins.

        Args:
            num_games (int): Number of games to run.

        Returns:
            float: Percentage of games won.
        """
        wins = 0
        for _ in range(num_games):
            game_instance = MinesweeperGame(8, 8, 10, gui=False)  # Set gui to False
            self.game = game_instance
            self.first_click()
            while not self.game.game_over:
                self.step_solve()
            if self.game.check_win():
                wins += 1
        return wins / num_games * 100  # Pourcentage de victoires


