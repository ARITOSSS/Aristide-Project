# Aristide-Project

## **Overview :**

My project implements a Minesweeper game solver :
- **Double Set Single Point (DSSP) Algorithm**: Algorithm that maintains two sets: one for certain cells and one for insecure cells, allowing more efficient flagging and probing.

The solver work by simulating a Minesweeper game, probing cells, and marking potential bombs until the game is won or lost.

## **Features :**

- **Minesweeper Game**: A fully functional Minesweeper game engine supporting different grid sizes and bomb configurations.
- **DSSP Algorithm**: Solver.
- **Unittest Support**: Comprehensive test cases for the game and solvers.
- **Pylint Support**: Ensures the code follows best practices in terms of structure, style, and quality.

  
## **Installation :**
- Clone the repisotory
  ```bash
  git clone https://github.com/ARITOSSS/Aristide-Project.git

- Open it in your IDE and
  ```bash
  cd .\Codes

## **Commands** :
- Pylint
  ```bash
  pylint .\name_of_the_file.py

- Unittest
  ```bash
  python -m coverage run -m unittest

- Coverage
  ```bash
  coverage report -m