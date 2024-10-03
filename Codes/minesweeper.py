import random
import tkinter as tk  # Pour l'interface graphique
from tkinter import messagebox

class MinesweeperGame:
    def __init__(self, rows: int, cols: int, num_bombs: int, gui: bool = True):
        self.grid_size = (rows, cols)
        self.num_bombs = num_bombs
        self.bomb_locations = []
        self.revealed_cells = set()
        self.flags = set()
        self.game_over = False
        self.first_click = None
        self.gui = gui
        self.buttons = {}
        
        if self.gui:
            self.window = tk.Tk()
            self.window.title("Minesweeper")
            self.setup_gui(rows, cols)

    def setup_gui(self, rows, cols):
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
        if self.gui:
            self.window.mainloop()

    def process_event(self, cell: tuple):
        if self.game_over or cell in self.revealed_cells:
            return

        if self.first_click is None:
            self.first_click = cell
            self.bomb_locations = self.generate_bomb_locations(
                self.grid_size[0],
                self.grid_size[1],
                self.num_bombs,
                self.first_click
            )
            self.reveal_initial_safe_zone(cell)

        if cell in self.bomb_locations:
            self.game_over = True
            if self.gui:
                self.reveal_bombs()
                messagebox.showinfo("Lost", "Bomb! You lost.")
            return

        self.reveal_cell(cell)

        if self.check_win():
            self.game_over = True
            if self.gui:
                messagebox.showinfo("Won", "Congratulations, you won!")

    def reveal_bombs(self):
        for bomb in self.bomb_locations:
            if self.gui:
                self.buttons[bomb].config(text='B', bg='red')

    def reveal_cell(self, cell: tuple):
        if cell in self.revealed_cells or cell in self.flags:
            return

        self.revealed_cells.add(cell)
        adjacent_bombs = self.count_adjacent_bombs(cell)
        button = self.buttons[cell] if self.gui else None
        if button:
            button.config(
                text=str(adjacent_bombs) if adjacent_bombs > 0 else '',
                state=tk.DISABLED,
                bg='light grey'
            )

        if adjacent_bombs == 0:
            for neighbor in self.get_neighbors(cell):
                self.reveal_cell(neighbor)

    def count_adjacent_bombs(self, cell: tuple) -> int:
        neighbors = self.get_neighbors(cell)
        return sum(1 for neighbor in neighbors if neighbor in self.bomb_locations)

    def get_neighbors(self, cell: tuple) -> list:
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

    def place_flag(self, cell: tuple):
        if cell not in self.revealed_cells:
            if cell in self.flags:
                self.flags.remove(cell)
                if self.gui:
                    self.buttons[cell].config(text='', bg='SystemButtonFace')
            else:
                self.flags.add(cell)
                if self.gui:
                    self.buttons[cell].config(text='F', bg='yellow')

    def check_win(self) -> bool:
        total_cells = self.grid_size[0] * self.grid_size[1]
        return len(self.revealed_cells) == total_cells - len(self.bomb_locations)

    def generate_bomb_locations(self, rows: int, cols: int, num_bombs: int, first_click: tuple) -> list:
        bomb_locations = set()
        safe_zone = set(self.get_neighbors(first_click) + [first_click])
        while len(bomb_locations) < num_bombs:
            location = (random.randint(0, rows - 1), random.randint(0, cols - 1))
            if location not in safe_zone and location not in bomb_locations:
                bomb_locations.add(location)
        return list(bomb_locations)

    def reveal_initial_safe_zone(self, cell: tuple):
        self.reveal_cell(cell)
        neighbors = self.get_neighbors(cell)
        revealed_cells = 1
        for neighbor in neighbors:
            if revealed_cells >= 0.15 * self.grid_size[0] * self.grid_size[1]:
                break
            if neighbor not in self.bomb_locations:
                self.reveal_cell(neighbor)
                revealed_cells += 1

    def get_label(self, cell: tuple) -> int:
        """Get the label (number of adjacent bombs) for a cell."""
        return self.count_adjacent_bombs(cell)  # Use the existing method to count adjacent bombs
