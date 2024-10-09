# Specification Document

## **General Structure of the Program :**
The Minesweeper program is split into two main components:

### **Minesweeper Game Logic :**

This module implements the core game logic of Minesweeper, including grid setup, bomb placement, user interactions, and game state management. It is structured using an object-oriented approach in the class [MinesweeperGame](https://github.com/ARITOSSS/Aristide-Project/blob/main/Codes/minesweeper.py), which encapsulates all attributes related to the game's state (grid size, bomb locations, revealed cells, etc.) and methods to handle events (such as revealing a cell or placing a flag). The game is designed to support both a graphical user interface (GUI) using Tkinter and a non-GUI version for testing purposes. It is important to note that this implementation of the deminer is designed to be solved by a solver and not by a human user.

### **Double Set Single Point (DSSP) Solver :**

The [DSSP Solver](https://github.com/ARITOSSS/Aristide-Project/blob/main/Codes/dssp_solver.py) begins by selecting a random cell and placing it in `Set S` (Certain Cells). Upon launching the algorithm, if `S` is not empty, it reveals the cell. It then checks for `AFN` (Adjacent Flagged Neighbors) to identify safe cells, which are added to `S`, while uncertain cells are placed in `Set Q` (Uncertain Cells). The algorithm then iterates through `Q`, using the information gathered from `S` to determine if it can safely reclassify certain cells or place flags using `iSAMN`. This process repeats in a loop until the game is either lost or won. If at any point `S` becomes empty, the algorithm will randomly select a cell to reveal.

## **Time and Space Complexities :**

### **Minesweeper Game Logic :**

#### **Time Complexity :**

- **Grid Initialization:** O(n), where n is the number of cells. This involves placing bombs randomly and setting up the game grid.
- **Revealing a Cell:** For each cell, the number of adjacent cells to check is constant (8 neighbors), leading to an O(1) operation per cell reveal. However, revealing all safe cells can cascade and potentially reveal large sections of the board, making it O(n) in the worst case.
- **Flagging a Cell:** Flagging or unflagging a cell takes constant time, O(1).

#### **Space Complexity :**

The game requires space to store the grid, bomb locations, revealed cells, and flags, leading to a space complexity of O(n), where n is the number of cells.

### **Double Set Single Point (DSSP) Solver :**

#### **Time Complexity :**

The time complexity of the DSSP solver is O(n²) due to the need to process potentially multiple interactions between uncertain cells. As the algorithm iterates over the grid, it checks relationships and counts for uncertain cells, leading to an increased number of operations.

#### **Space Complexity :**

DSSP maintains two sets (S and Q) for certain and uncertain cells, contributing to a space complexity of O(n). This remains efficient as it only stores references to cells rather than duplicating data.

### **Performance and Big O Analysis Comparison :**

The DSSP algorithm has a time complexity of O(n²), which is higher than the linear complexity of the game logic. However, this added complexity allows DSSP to make more informed decisions regarding uncertain cells, ultimately leading to a higher success rate in solving challenging board setups compared to naive approaches.

## **Potential Shortcomings and Suggested Improvements :**

### Double Set Single Point (DSSP) Solver :**

#### **Notes:**

- The DSSP algorithm can still fail in very complex scenarios where uncertain cells create complex dependencies, which can lead to incorrect inferences.
- Increasing time complexity could lead to slower performance on larger grids.

#### **Improvements:**

- Introduce a heuristic to prioritise the probing of cells based on certain criteria (for example, proximity to reported bombs or a high number of adjacent unknown cells). In particular, by seeing the deminer as a constraint satisfaction problem.

## **Use of Extensive Language Models (ChatGPT, etc.) :**

ChatGPT and DeepL are the only external tools I have used for various reasons:
- For reports and documentation, I always act in the same way: first, I write a base in French, which I have corrected by ChatGPT and which I then translate into English with DeepL.
- I generate the docstrings with ChatGPT and then modify them in my own way.
- I use ChatGPT when I'm having trouble understanding something I don't know, such as the use of graphical interfaces, pylint, unittest, or even certain errors. Beyond that, I avoid using code generated via ChatGPT because I have the impression that it more often ends up causing problems than anything else, but I draw inspiration from it.

## **References :**

- [Harvard DASH](https://dash.harvard.edu/handle/1/14398552)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Pylint Tutorial](https://gamedevacademy.org/pylint-tutorial-complete-guide/)
- [Python Unittest Coverage](https://www.pythontutorial.net/python-unit-testing/python-unittest-coverage/)
- [Caml Documentation](https://caml.inria.fr/pub/docs/oreilly-book/html/book-ora059.html#:~:text=At%20the%20beginning%20of%20the,up%20and%20the%20player%20loses.)
