# Research Paper
Name: Zixi Li

Semester: Spring 2023

Topic: Analysis of Alpha-Beta Pruning and Minimax Algorithms

Link The Repository: https://github.com/christinalizx/Minimax_abp_research.git

## Introduction
Minimax is a recursive search algorithm that is widely used in decision making and game theory. It uses recursion to search in a tree using depth-first search method. There is a maximizer and a minimizer in the algorithm, each one provides an optimal move and assuming the other one is making the optimal move as well. It will proceed to the terminal node of the tree, and backtrack the tree recursively.
Alpha-Beta Pruning (ABP) is an optimization of Minimax. It seeks to decrease the number of nodes that the Minimax has to search for in a tree. It stops evaluating a move when the branches of the tree that are unlikely to lead to a better outcome[^1]. This is achieved by keeping track of lower and upper bounds on the scores that can be achieved from certain moves and not evaluating nodes that fall outside of these bounds. Therefore, the ABP runs faster than Minimax in searching a tree.

Minimax and ABP are commonly used in artificial intelligence (AI) and game theory to solve problems related to game-playing, such as finding the best move in complex games like chess, Tictactoe, connect4 etc, where each player tries to maximize their own score and minimize their opponent's score.

Minimax was first proposed by John von Neumann in the 1920s as a way to solve two-player zero-sum games such as chess, checkers, and Go. The algorithm was later refined by other researchers, including John Nash, who introduced the concept of Nash equilibrium in game theory.

ABP was introduced by John McCarthy and his colleagues in the late 1950s as a way to improve the efficiency of the minimax algorithm by reducing the number of nodes that need to be evaluated. The algorithm was inspired by ideas from the minimax algorithm and the principle of branch-and-bound in optimization[^2].

This paper will first provide a detailed analysis of these two algorithms through time and space complexity. Then, it is going to analyze the runtime performance of the minimax algorithm and the abp algorithm through implementing these two algorithms to a game called connect4. Due to the intensity of time, the game is a depth-limited version of connect4 borrowed the GUI interface from Pei Xu(peix@g.clemson.edu), but the algorithms are implemented as individual efforts. The paper is seeking to compare the performance of each of these two algorithms by initiating two players, one is the maximizing player while the other is the minimizing player. The user has a choice to choose whether it is minimax vs. minimax or minimax vs. abp. The user also has an option to choose play against the minimax or abp AI player. The runtime analysis will be presented by line chart, and the results of the game play will be shown in graphics. Language analysis will be presented.

[^1]: "Alpha-Beta pruning": https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#:~:text=Alpha%E2%80%93beta%20pruning%20is%20a,Connect%204%2C%20etc
[^2]: "Russell, S. J., & Norvig, P. (2010). Artificial intelligence: A modern approach (3rd ed.). Prentice Hall. p193-195": https://scholar.alaqsa.edu.ps/9195/1/Artificial%20Intelligence%20A%20Modern%20Approach%20%283rd%20Edition%29.pdf%20%28%20PDFDrive%20%29.pdf


## Analysis of Algorithm/Datastructure
Make sure to include the following:
- Time Complexity
- Space Complexity
- General analysis of the algorithm/datastructure

## Empirical Analysis
- What is the empirical analysis?
- Provide specific examples / data.


## Application
- What is the algorithm/datastructure used for?
- Provide specific examples
- Why is it useful / used in that field area?
- Make sure to provide sources for your information.


## Implementation
- What language did you use?
- What libraries did you use?
- What were the challenges you faced?
- Provide key points of the algorithm/datastructure implementation, discuss the code.
- If you found code in another language, and then implemented in your own language that is fine - but make sure to document that.


## Summary
- Provide a summary of your findings
- What did you learn?