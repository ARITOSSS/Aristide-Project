"""
This module contains the implementation of the Minesweeper game logic,
including the game setup, processing user inputs, and managing game state.
"""

import random
import tkinter as tk  # Importing tkinter for creating the graphical user interface
from tkinter import messagebox

class MinesweeperGame:
    """
    Class representing the Minesweeper game.

    Attributes:
        grid_size (tuple): The size of the grid as (rows, columns).
        num_bombs (int): The total number of bombs in the game.
        bomb_locations (list): List of bomb locations.
        revealed_cells (set): Set of revealed cells.
        flags (set): Set of flagged cells.
        game_over (bool): Indicates if the game is over.
        gui (bool): Indicates if the GUI is enabled.
        buttons (dict): Dictionary mapping cell coordinates to button objects.
        cols (int): Number of columns in the grid.
        rows (int): Number of rows in the grid.
    """

    def __init__(self, rows: int, cols: int, num_bombs: int, gui: bool = True):
        """
        Initialize the Minesweeper game with the given parameters.

        Args:
            rows (int): Number of rows in the grid.
            cols (int): Number of columns in the grid.
            num_bombs (int): Number of bombs in the game.
            gui (bool): If True, the GUI will be enabled.
        """
        self.grid_size = (rows, cols)
        self.num_bombs = num_bombs
        self.bomb_locations = self.generate_bomb_locations(rows, cols, num_bombs)
        self.revealed_cells = set()
        self.flags = set()
        self.game_over = False
        self.gui = gui
        self.buttons = {}
        self.cols = cols
        self.rows = rows
        if self.gui:
            self.window = tk.Tk()  # Create a new Tkinter window
            self.window.title("Minesweeper")  # Set the title of the window
            self.setup_gui(rows, cols)  # Set up the GUI

    def setup_gui(self, rows, cols):
        """
        Set up the graphical user interface for the Minesweeper game.
        
        Args:
            rows (int): The number of rows in the game grid.
            cols (int): The number of columns in the game grid.
        """
        for row in range(rows):
            for col in range(cols):
                # Create a button for each cell, linked to the process_event method
                button = tk.Button(
                    self.window, width=2, height=1,
                    command=lambda r=row, c=col: self.process_event((r, c))
                )
                # Bind right-click to place a flag on the cell
                button.bind(
                    '<Button-3>',
                    lambda event, r=row, c=col: self.place_flag((r, c))
                )
                button.grid(row=row, column=col)  # Place button in the grid
                self.buttons[(row, col)] = button  # Map coordinates to button

    def start_game(self):
        """
        Start the game and enter the GUI main loop.
        """
        if self.gui:
            self.window.mainloop()  # Start the Tkinter event loop

    def process_event(self, cell: tuple):
        """
        Process the user's click on a cell.

        Args:
            cell (tuple): The (row, column) coordinates of the cell clicked.
        """
        if cell in self.bomb_locations:
            self.game_over = True
            if self.gui:
                self.reveal_bombs()  # Reveal all bombs
                messagebox.showinfo("Lost", "Bomb! You lost.")  # Show message box
            return
        self.reveal_cell(cell)

        if self.check_win():
            self.game_over = True
            if self.gui:
                messagebox.showinfo("Won", "Congratulations, you won!")  # Show win message

    def reveal_bombs(self):
        """
        Reveal all bomb locations when the game is over.
        """
        for bomb in self.bomb_locations:  # Loop through all bomb locations
            if self.gui:
                self.buttons[bomb].config(text='B', bg='red')  # Change button to show bomb

    def reveal_cell(self, cell: tuple):
        """
        Reveal a cell and display the number of adjacent bombs.

        Args:
            cell (tuple): The (row, column) coordinates of the cell to reveal.
        """
        if cell in self.revealed_cells or cell in self.flags:
            return

        self.revealed_cells.add(cell)  # Add cell to revealed cells
        adjacent_bombs = self.count_adjacent_bombs(cell)  # Count adjacent bombs
        button = self.buttons[cell] if self.gui else None  # Get button reference if GUI is enabled
        if button:
            button.config(
                text=str(adjacent_bombs) if adjacent_bombs > 0 else '',  # Show bomb count or empty
                state=tk.DISABLED,  # Disable button to prevent further clicks
                bg='light grey'  # Change background color
            )

    def count_adjacent_bombs(self, cell: tuple) -> int:
        """
        Count the number of bombs adjacent to a given cell.

        Args:
            cell (tuple): The (row, column) coordinates of the cell.

        Returns:
            int: The number of bombs adjacent to the cell.
        """
        neighbors = self.get_neighbors(cell)  # Get neighboring cells
        return sum(1 for neighbor in neighbors if neighbor in self.bomb_locations)  # Count bombs

    def get_neighbors(self, cell: tuple) -> list:
        """
        Get the list of neighboring cells for a given cell.

        Args:
            cell (tuple): The (row, column) coordinates of the cell.

        Returns:
            list: List of neighboring cell coordinates.
        """
        # Extract the row and column from the cell
        row, col = cell
        rows, cols = self.grid_size  # Get total rows and columns
        neighbors = []  # Initialize list for neighbors
        # Loop through possible neighbor offsets
        for dr in [-1, 0, 1]:  # Row offsets (-1, 0, 1)
            for dc in [-1, 0, 1]:  # Column offsets (-1, 0, 1)
                if dr == 0 and dc == 0:  # Skip the current cell
                    continue
                neighbor = (row + dr, col + dc)  # Calculate neighbor coordinates
                # Check if the neighbor is within bounds
                if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                    neighbors.append(neighbor)  # Add valid neighbor to the list
        return neighbors  # Return the list of neighboring cells

    def place_flag(self, cell: tuple):
        """
        Place or remove a flag on a cell.

        Args:
            cell (tuple): The (row, column) coordinates of the cell.
        """
        if cell not in self.revealed_cells:  # Only place a flag on unrevealed cells
            if cell in self.flags:  # If the cell is already flagged
                self.flags.remove(cell)  # Remove the flag
                if self.gui:
                    self.buttons[cell].config(text='', bg='SystemButtonFace')
            else:  # If the cell is not flagged
                self.flags.add(cell)  # Add the flag
                if self.gui:
                    self.buttons[cell].config(text='F', bg='yellow')

    def check_win(self) -> bool:
        """
        Check if the player has won the game.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        total_cells = self.grid_size[0] * self.grid_size[1]
        return len(self.revealed_cells) == total_cells - len(self.bomb_locations)


    def generate_bomb_locations(self, rows: int, cols: int, num_bombs: int):
        """
        Generate a set of random bomb locations.

        Args:
            rows (int): The number of rows in the grid.
            cols (int): The number of columns in the grid.
            num_bombs (int): The number of bombs to place.

        Returns:
            list: A list of bomb locations as tuples.
        """
        bomb_locations = set()
        while len(bomb_locations) < num_bombs:
            location = (random.randint(0, rows - 1), random.randint(0, cols - 1))
            if location not in bomb_locations:
                bomb_locations.add(location)
        return list(bomb_locations)



if __name__ == "__main__":
    game = MinesweeperGame(9, 9, 10)
    game.start_game()