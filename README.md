# Aristide-Project

## **Overview :**

My project implements a Minesweeper game solver using two main algorithms:
- **Naive Single Point (NSP) Algorithm**: A basic approach for solving Minesweeper by probing random cells and using local bomb information to deduce the status of neighboring cells.
- **Double Set Single Point (DSSP) Algorithm**: A more advanced algorithm that maintains two sets: one for certain cells and one for insecure cells, allowing more efficient flagging and probing.

The solver works by simulating a Minesweeper game, probing cells, and marking potential bombs until the game is won or lost.

## **Features :**

- **Minesweeper Game**: A fully functional Minesweeper game engine supporting different grid sizes and bomb configurations.
- **NSP Algorithm**: Solves the Minesweeper game using basic heuristics.
- **DSSP Algorithm**: A more sophisticated solver that improves the chances of solving the game by reducing unnecessary probes.
- **Unittest Support**: Comprehensive test cases for the game and solvers.
- **Pylint Support**: Ensures the code follows best practices in terms of structure, style, and quality.

## **Requirements :**
- Python 3.8+
- Required libraries:
  ```bash
  pip install pylint

  
## **Installation :**
- Clone the repisotory
  ```bash
  git clone https://github.com/ARITOSSS/Aristide-Project.git

- Open it in your IDE and
  ```bash
  cd .\Codes

## **Commands** :
1. Pylint :
  ```bash
  pylint .\name_of_the_file.py
2. Unittest :
  ```bash
  python -m coverage run -m unittest
  coverage report -m
