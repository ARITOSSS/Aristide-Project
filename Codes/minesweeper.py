""" Basic Minesweeper """
import tkinter as tk
from tkinter import messagebox
import random


#Faire des vrais docs qui indique les paramètres et les retours de chaque fonction
class MinesweeperSolver:
    """Class to implement Minesweeper game with GUI and solver logic."""    
    def __init__(self, rows, cols, num_bombs):
        self.grid_size = (rows, cols)
        self.num_bombs = num_bombs
        self.bomb_locations = []
        self.revealed_cells = set()
        self.flags = set()
        self.game_over = False
        self.first_click = None

        self.window = tk.Tk()
        self.window.title("Minesweeper")

        self.buttons = {}
        for row in range(rows):
            for col in range(cols):
                button = tk.Button(
                    self.window, width=2, height=1,
                    command=lambda r=row, c=col: self.process_event((r, c))
                )
                button.bind(
                    '<Button-3>',
                    lambda event, r=row, c=col: self.place_flag((r, c))
                )
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button

    def start_game(self):
        """Start the game loop."""
        self.window.mainloop()

    def process_event(self, cell):
        """Handle left-click event on a cell."""
        if self.game_over or cell in self.revealed_cells:
            return

        if self.first_click is None:
            self.first_click = cell
            self.bomb_locations = self.generate_bomb_locations(self.grid_size[0],
            self.grid_size[1], self.num_bombs, self.first_click)
            self.reveal_initial_safe_zone(cell)

        if cell in self.bomb_locations:
            self.reveal_bombs()
            self.game_over = True
            messagebox.showinfo("Lost", "Bomb! You lost.")
            return

        self.reveal_cell(cell)

        if self.check_win():
            self.game_over = True
            messagebox.showinfo("Won", "Congratulations, you won!")

    def reveal_bombs(self):
        """Reveal all bombs on the grid."""
        for bomb in self.bomb_locations:
            self.buttons[bomb].config(text='B', bg='red')

    def reveal_cell(self, cell):
        """Reveal a cell and its adjacent cells if necessary."""
        if cell in self.revealed_cells or cell in self.flags:
            return

        self.revealed_cells.add(cell)
        adjacent_bombs = self.count_adjacent_bombs(cell)
        button = self.buttons[cell]
        button.config(
            text=str(adjacent_bombs) if adjacent_bombs > 0 else '',
            state=tk.DISABLED,
            bg='light grey'
        )

        if adjacent_bombs == 0:
            for neighbor in self.get_neighbors(cell):
                self.reveal_cell(neighbor)

    def count_adjacent_bombs(self, cell):
        """Count bombs in neighboring cells."""
        neighbors = self.get_neighbors(cell)
        return sum(1 for neighbor in neighbors if neighbor in self.bomb_locations)

    def get_neighbors(self, cell):
        """Get valid neighboring cells for a given cell."""
        row, col = cell
        rows, cols = self.grid_size
        neighbors = []

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                neighbor = (row + dr, col + dc)
                if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                    neighbors.append(neighbor)

        return neighbors

    def place_flag(self, cell):
        """Place or remove a flag on a cell."""
        if cell not in self.revealed_cells:
            if cell in self.flags:
                self.flags.remove(cell)
                self.buttons[cell].config(text='', bg='SystemButtonFace')
            else:
                self.flags.add(cell)
                self.buttons[cell].config(text='F', bg='yellow')

    def check_win(self):
        """Check if the player has won the game."""
        total_cells = self.grid_size[0] * self.grid_size[1]
        return len(self.revealed_cells) == total_cells - len(self.bomb_locations)

    def generate_bomb_locations(self, rows, cols, num_bombs, first_click):
        """Generate bomb locations ensuring the first click is safe."""
        bomb_locations = set()
        safe_zone = set(self.get_neighbors(first_click) + [first_click])

        while len(bomb_locations) < num_bombs:
            location = (random.randint(0, rows - 1), random.randint(0, cols - 1))
            if location not in safe_zone and location not in bomb_locations:
                bomb_locations.add(location)

        return list(bomb_locations)

    def reveal_initial_safe_zone(self, cell):
        """Reveal a zone around the first click to ensure at least 15% of the board is revealed."""
        self.reveal_cell(cell)
        neighbors = self.get_neighbors(cell)
        revealed_cells = 1  # Start with the first clicked cell
        for neighbor in neighbors:
            if revealed_cells >= 0.15 * self.grid_size[0] * self.grid_size[1]:
                break
            if neighbor not in self.bomb_locations:
                self.reveal_cell(neighbor)
                revealed_cells += 1


def choose_difficulty():
    """Display difficulty selection window."""
    def set_difficulty(difficulty):
        if difficulty == "Beginner":
            rows, cols, bombs = 8, 10, 10
        elif difficulty == "Intermediate":
            rows, cols, bombs = 14, 18, 40
        elif difficulty == "Advanced":
            rows, cols, bombs = 20, 30, 99
        else:
            return

        difficulty_window.destroy()
        solver = MinesweeperSolver(rows, cols, bombs)
        solver.start_game()

    difficulty_window = tk.Tk()
    difficulty_window.title("Select Difficulty")

    tk.Button(difficulty_window,
              text="Beginner", command=lambda: set_difficulty("Beginner")).pack(fill=tk.X)
    tk.Button(difficulty_window,
              text="Intermediate", command=lambda: set_difficulty("Intermediate")).pack(fill=tk.X)
    tk.Button(difficulty_window,
              text="Advanced", command=lambda: set_difficulty("Advanced")).pack(fill=tk.X)

    difficulty_window.mainloop()


if __name__ == "__main__":
    choose_difficulty()
