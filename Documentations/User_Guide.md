# User Guide for Minesweeper Solver using DSSP Algorithm

---

## **1. How to use the Program :**

### **Pre-requisites :**

Before running the program, ensure that the required libraries are installed. Run the following command to install the necessary packages:

```bash
pip install unittest numpy matplotlib tkinter coverage pylint
```

### Steps to Run the Program :
- Navigate to the ".\Codes" Folder :

#### **Running the Minesweeper Game :**
- Use this command :
```bash
python main.py
```

#### **See how clean the code is :**
```bash
pylint .\dssp_solver.py .\test_dssp_solver.py .\test_minesweeper.py .\statistics.py .\main.py .\minesweeper.py
```

#### **Most important file is [statistics.py](https://github.com/ARITOSSS/Aristide-Project/blob/main/Codes/statistics.py) :**
This file is the most important, because what's interesting for my project is to see the results obtained by the algorithm on several deminer difficulties. The main file is just for fun, so you can see how each iteration of the algorithm performs. This file wrote the result in [Testing_Document](https://github.com/ARITOSSS/Aristide-Project/blob/main/Documentations/Testing_Document.md).

---

## **2. Functionalities of the Program :**

### **A. MinesweeperGame :**

The  `MinesweeperGame` class in [minesweeper.py](https://github.com/ARITOSSS/Aristide-Project/blob/main/Codes/minesweeper.py) manages the Minesweeper game logic. Please note that this version is designed for use with a solver, so it cannot be played as a conventional Minesweeper game. Here's how the game functions :

- **Grid Initialization** : The game is initialized with a grid of specified size and number of bombs. Like `MineSweeperGame(9,9,10)` starts a game with a 9x9 grid and 10 bombs.

- **User Interface** : If `gui=True`(default), a graphical interface is created using Tkinter, allowing you to see the solver in action. For all the tests and in `run_games` function i set this to False. 

- **Revealing Cells** : Clicking a cell reveals its content (bomb, empty, or number of adjacent bombs).`reveal_cell`

- **Flagging Cells** : Right-clicking a cell allows you to place a flag to mark potential bombs.Place flag to mark potential bombs.`place_flag`

- **Win/Loss Conditions :** You win the game if all non-bomb cells are revealed, and you lose if you click on a bomb.`check_win`

- **Other functions :** The other functions allow you to reveal all the bombs when you click on one, to obtain an array containing the neighbours of a square, to obtain the number of adjacent bombs... They help to make the game more coherent and to make DSSP work, in particular `get_neighbors`.

### **B. DSSP Solver :**

The `MinesweeperSolverDSSP` class in [dssp_solver.py](https://github.com/ARITOSSS/Aristide-Project/blob/main/Codes/dspp_solver.py.py) implements the **Double Set Single Point** algorithm to automatically play the game.

- **Initial Move :** The solver selects an initial `opener` cell randomly. `select_random`.

- **Identifying Safe Cells :** The algorithm identifies cells that are safe to reveal based on the neighboring flags and bombs. `isAFN`

- **Flagging Mines :** If a cell's neigbors are confirmed as bombs, the solver flags them. ``isAMN``

- **End of Game** : `step_solve` use these three functions to solve the game untils the game is wins or lost.

## **Input Format for the Program :**
There is not a lot of input in my program and they are all in `main.py` or `statistics.py`.

- `game = MinesweeperGame(9,9,10)` : Create a game with input `rows` **int**, `colums` **int** and `number of bombs` **int**.

- `solver = MinesweeperSolverDSSP(game)` : Allows a game to be associated with a solver, input `game` **MinesweeperGame**.

- ` solver.run_games(1000, 9, 9, 10)` : `Number of games` **int** and the following inputs are to generate a minesweeper game, so row col and nb_bombs.

In general, the other functions in my program take a cell as input, which is represented as a tuple. This tuple typically contains two elements: the row coordinate and the column coordinate of the cell on the game board. This allows for easy identification of each cell when executing various functions related to game manipulation and analysis.



