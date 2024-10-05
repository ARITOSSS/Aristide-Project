# Specification Document

## **General Structure of the Program :**
The Minesweeper program is split into three main components:

### **Minesweeper Game Logic :**

This module implements the core game logic of Minesweeper, including grid setup, bomb placement, user interactions, and game state management.
It is structured using an object-oriented approach in the class MinesweeperGame, which encapsulates all attributes related to the game's state (grid size, bomb locations, revealed cells, etc.) and methods to handle events (such as revealing a cell or placing a flag).
The game is designed to support both a graphical user interface (GUI) using Tkinter and a non-GUI version for testing purposes.

### **Naive Single Point (NSP) Solver :**

This solver implements a simple approach to solving Minesweeper by processing individual cells one at a time.
It iterates over the grid, probing cells, flagging bombs, and attempting to deduce safe cells based on the number of adjacent bombs.
The core operations include selecting random unexplored cells and using basic rules (isAFN/isAMN) to mark cells as safe or to place flags.

### **Double Set Single Point (DSSP) Solver :**

A more advanced solver that leverages two sets: S (certain cells) and Q (uncertain cells).
It performs a similar function to the NSP solver but with enhanced logic for handling uncertain cells, allowing more advanced deductions and flag placements.

## **Time and Space Complexities :**

### **Minesweeper Game Logic :**

#### **Time Complexity :**

Grid Initialization: 

O(n), where n is the number of cells. This involves placing bombs randomly and setting up the game grid.

Revealing a Cell: For each cell, the number of adjacent cells to check is constant (8 neighbors), leading to an O(1) operation per cell reveal. However, revealing all safe cells can cascade and potentially reveal large sections of the board, making it 

O(n) in the worst case.

Flagging a Cell: Flagging or unflagging a cell takes constant time, 

O(1).

#### **Space Complexity :**

The game requires space to store the grid, bomb locations, revealed cells, and flags, leading to a space complexity of 
O(n), where n is the number of cells. 

### **Naive Single Point (NSP) Solver : **

#### **Time Complexity :**

Modify here

#### **Space Complexity :**

The solver maintains sets for cells to probe and flags, contributing to a space complexity of O(n).


### **Double Set Single Point (DSSP) Solver :**

#### **Time Complexity : **

Modify here

#### **Space Complexity :**
DSSP also maintains two sets (S and Q), which increases space usage slightly, but the overall complexity is still O(n).


### **Performance and Big O Analysis Comparison : ** 
NSP vs. DSSP:
Both solvers operate with (Modify here with complexity) time complexity, but the DSSP algorithm has more intricate logic for handling uncertain cells. This added complexity improves decision-making but increases the overhead in each step, resulting in a higher constant factor in practice.
DSSP is more effective in complex board setups, as it is capable of handling uncertainty better by using two sets (S and Q). This makes it more likely to win difficult games compared to NSP, which is purely naive in its approach.


## **Potential Shortcomings and Suggested Improvements :**

### **Minesweeper Game Logic :**

#### **Shortcomings :**

Do this last week

#### **Improvements :**

Do this last week


### **Naive Single Point (NSP) Solver :**

#### **Shortcomings :**

Do this last week

#### **Improvements :**

Do this last week

### **Double Set Single Point (DSSP) Solver :**

#### **Shortcomings :**

Do this last week

#### **Improvements :**

Do this last week

## **Use of Extensive Language Models (ChatGPT, etc.) :**

ChatGPT and DeepL are the only external tools I have used for various reasons:
- For reports and documentation, I always act in the same way: first I write a base in French, which I have corrected by chatGpt and which I then translate into English with Deepl.
- I generate the docstrings with ChatGpt and then modify them in my own way.
- Otherwise I use ChatGpt when I'm having trouble understanding something I don't know, such as the use of graphical interfaces, pylint, unittest or even certain errors. Beyond that, I avoid using code generated via ChatGpt because I have the impression that it more often ends up causing problems than anything else, but I draw inspiration from it.


## **References : **
https://dash.harvard.edu/handle/1/14398552
https://docs.python.org/3/library/tkinter.html
https://gamedevacademy.org/pylint-tutorial-complete-guide/
https://www.pythontutorial.net/python-unit-testing/python-unittest-coverage/
https://caml.inria.fr/pub/docs/oreilly-book/html/book-ora059.html#:~:text=At%20the%20beginning%20of%20the,up%20and%20the%20player%20loses.