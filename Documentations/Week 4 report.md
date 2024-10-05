# Weekly Report 4

## **Time spent on the project :**
8.5 Hours

## **What have you done this week ?**
This week, I focused on resolving the issues I encountered with my Minesweeper solving algorithm. I dedicated significant time to debugging the algorithm, which helped identify and fix several critical errors. Additionally, I worked on ensuring that my code adheres to the Pylint standards, enhancing its readability and maintainability.

After addressing the algorithm's weaknesses, I began developing unit tests to further validate its functionality. 

## **How has the project progressed ?**
The project has progressed positively this week. The algorithm is now functioning more reliably, with the previous issues largely resolved. By aligning the code with Pylint standards, I have improved its quality and set a foundation for future developments. The introduction of unit tests marks a significant step toward ensuring the robustness of the code.

## **What did you learn this week ?**
This weekend I learnt that it's sometimes important to get away from the keyboard and sit down in front of your code to try and simplify it or make it more efficient when you're stuck. So I took some time to identify potential problems in my current code, which I corrected one by one. I also divided the step_solve function into several sub-functions to improve readability.

## **What has been unclear or problematic ?**
As I didn't necessarily have the opportunity to work on the testing part before doing this project, I'm not sure about the quality of my tests and I'd like some feedback if possible to find out if I'm doing it the right way. My tests on the basic minesweeper look OK to me, but those on my solver just give me the impression that I'm working around the problem in order to get a good coverage score. Particularly with the use of MagicMock, which seems strange to me

## **What’s next ?**
My plans for the week ahead include :

Improve my tests
Do the pear-review
If time allows, I will begin working on the implementation of the Double Set Single Point algorithm and try to implement a tool that will allow me to see the success rate of my algorithm

## **Questions : **
Would it be possible to get some feedback on how I'm doing my tests ?
I've implemented my own vision of the thing for the first click which is particular to the deminer who hasn't found any sources on the internet. On the first click I reveal about 15% of the squares around the click and place the bombs afterwards. My solver starts the game with a random click and will sometimes click in places that are not very advantageous, such as corners or edges, where clicking in the middle would give him a more advantageous position. Should I keep the fact that he clicks randomly or should I make him start in an advantageous position?

