# Weekly Report 2

## **Time spent on the project :**
12 Hours

## **What have you done this week ?**
This week, I made significant progress on the project by implementing the graphical interface and the corresponding code that allows playing Minesweeper directly via the interface. I added three difficulty levels, each of which adjusts the total number of cells and bombs accordingly.

I chose to make the interface playable to be able to test more quickly whether my code worked and also for my personal use.

Initially, I experimented with several GUI libraries, trying to find one that suited my needs. I started with a large, somewhat messy block of code that didn’t work as expected, costing me a considerable amount of time. Once I realized the limitations of my initial approach, I decided to rework everything from scratch, organizing the code within a class. This improved the overall structure, making the code more efficient and easier to understand.

One of the more challenging aspects was handling the first click in Minesweeper, which is special since it needs to provide the player with an advantageous starting point. After some trial and error, I learned that the bombs should only be generated after the first click. Initially, I attempted to shift bombs that were already placed, but this caused problems. I eventually settled on revealing about 15% of the board around the first click to ensure a favorable starting position for the player.

After completing the core gameplay, I thoroughly commented my code and ensured that it adhered to coding standards, achieving a high score on pylint. I also began implementing unit tests using the unittest framework.

## **How has the project progressed ?**
The project has moved forward quite well this week, particularly with the successful implementation of the graphical interface and basic game logic for Minesweeper. The structure of the code has been significantly improved, and I've started laying the groundwork for testing. While there are still challenges ahead, particularly with the solver algorithm, this week marked an important step in bringing the project closer to completion.

## **What did you learn this week ?**
This week, I learned a great deal about structuring code more effectively, particularly the benefits of organizing logic into classes. This not only improved readability but also made it easier to extend and modify the project. I also gained a better understanding of GUI development and the challenges involved, particularly with game logic. Managing the special conditions for the first click in Minesweeper was a key learning experience. Additionally, I made progress in understanding unit testing practices in Python through the use of the unittest module.

## **What has been unclear or problematic ?**
The most challenging part of this week was handling the first click logic in Minesweeper. It took several iterations and approaches before I settled on generating the bombs after the first click to ensure a favorable starting condition for the player. Initially, my attempts to shift bombs that were already placed led to many issues, including unbalanced gameplay. Once I understood the root of the problem, I was able to simplify the solution, but this caused some frustration and delays.

Additionally, structuring the code efficiently was difficult at first. My initial attempt resulted in a strange codebase, which forced me to start over. While this was a learning experience, it took more time than expected.

## **What’s next ?**
Now all I have to do is complete my test file to get the last few percent remaining for 100% coverage and then I can concentrate on the solver algorithm.

First I'm going to find out how the algorithm works before trying to implement it.