# Specification Document

## **Me :**

Cligny Aristide - Exchange Students - Bachelor in Computer Science

## **Problem :**

The problem being solved is creating an AI that can effectively and efficiently play and solve the game of Minesweeper. The goal is to accurately identify safe cells and mines on the game board by combining deterministic and heuristic approaches. This involves using logical reasoning to make guaranteed safe moves (deterministic) and probabilistic assessment to handle uncertain situations (heuristic), all while minimizing incorrect guesses that could lead to losing the game.

## **Languages :**

For this project I chose to code in Python because it's the language I'm most comfortable with and it seems to me to be the most complete.

I think I'm capable of evaluating projects in Python, Java or C.

## Algorithms:

I plan to implement the Double Set Single Point (DSSP) algorithm, but as it is purely deterministic, its performance decreases as the size of the game increases. To remedy this, I'd like to incorporate a constraint satisfaction problem (CSP)-type approach if time permits, or else a heuristic solution to unlock more complex situations and thus increase the resolution rate. In addition, it should be noted that some parts of the deminer's game are impossible to win due to the presence of random factors in certain situations.

## Data Structures:

- **2D Arrays (Matrices):** The game board is represented using a 2D array to store the state of each cell (hidden, revealed, or flagged as a mine).
- **Sets and Lists:** These are used to keep track of revealed cells, flagged mines, and cells that need further examination.
- **Stack (for Backtracking):** Used to keep track of states during hypothesis testing when performing backtracking.

## **Complexities :**

Using the DSSP, the complexity is O(2^n) because as the dimensions of the grid increase, the resolution time increases exponentially.

The spatial complexity of 2D arrays is O(n) for the number of squares, and the same applies to sets and lists.

## **References :**

[https://dash.harvard.edu/handle/1/14398552](https://dash.harvard.edu/handle/1/14398552) (DSSP pseudo code and introduction to CSP)

[https://en.wikipedia.org/wiki/Minesweeper_(video_game)](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) ( Rules of the game)