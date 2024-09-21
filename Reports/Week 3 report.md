# Weekly Report 3

## **Time spent on the project :**
10 Hours

## **What have you done this week ? **
This week I focused on improving the unit tests for my Minesweeper codebase, with the aim of increasing test coverage. After improving the tests, I started work on implementing an algorithm to solve the Minesweeper. I therefore took the time to read the entire Harvard student thesis provided on moodle in the examples of Minesweeper solvers.(https://dash.harvard.edu/handle/1/14398552)

Initially, I intended to implement the Double Set Single Point algorithm directly, but after some experimentation, I realized it would be more efficient to first tackle the Naive version and then move on to the Double Single Point. Implementing the Naive Single Point algorithm posed several challenges, including Python's limitation of not allowing elements to be added to a set while iterating over it. This forced me to approach the problem differently.

Moreover, the pseudocode for the algorithm contained references to functions that were not explicitly provided, which meant I had to develop those functions from scratch. After multiple attempts and adjustments, I managed to create an algorithm that can solve simple Minesweeper boards. However, the solution still has some weaknesses, such as making incorrect decisions in certain scenarios.

## **How has the project progressed ?**
The project has made steady progress. I've managed to implement a basic version of the Naive Single Point algorithm, which is a critical step towards solving the Minesweeper maps. Although the current algorithm isn't perfect, it's a good base for me to build on in the coming weeks.

## **What did you learn this week ?**
This week, I learned several important lessons:

Algorithm implementation in Python: The difficulty of iterating and modifying sets in Python required a creative solution, which broadened my understanding of Python's data structures and iteration mechanisms.
Breaking down complex algorithms: Starting with the Naive Single Point before moving to the more complex Double Single Point proved to be a better strategy, helping me build up the logic step by step.


## **What has been unclear or problematic ?**
One of the main challenges this week was Python's restriction on modifying a set during iteration. This caused several problems on my first attempts, and it took several iterations to find a solution. These difficulties slowed my progress, and although my version of the Naive Single Point algorithm sometimes manages to solve a simple demineraliser, it still struggles in some particular cases, making sub-optimal decisions.

## **What’s next ?**
Next week, I'll be concentrating on refining the Naive Single Point algorithm to remedy its current shortcomings. 

I plan to:
Refactor the existing code to improve clarity and efficiency.
Add comments to ensure the code is well documented and easy to follow.
Run tests and test the quality of the code using pylint and coverage.
If I manage to do all that I'll start work on implementing the Double Set Single Point.
