# Research Paper
Name: Zixi Li

Semester: Spring 2023

Topic: Analysis of Alpha-Beta Pruning and Minimax Algorithms

Link The Repository: https://github.com/christinalizx/Minimax_abp_research.git

## Introduction
Minimax is a recursive search algorithm that is widely used in decision making and game theory. It uses recursion to search in a tree using depth-first search method. There is a maximizer and a minimizer in the algorithm, each one provides an optimal move and assuming the other one is making the optimal move as well. It will proceed to the terminal node of the tree, and backtrack the tree recursively.
Alpha-Beta Pruning (ABP) is not a brand new algorithm, it is an optimization of Minimax. It seeks to decrease the number of nodes that the Minimax has to search for in a tree. It stops evaluating a move when the branches of the tree that are unlikely to lead to a better outcome[^1]. This is achieved by keeping track of lower and upper bounds on the scores that can be achieved from certain moves and not evaluating nodes that fall outside of these bounds. Therefore, the ABP runs faster than Minimax in searching a tree.

Minimax and ABP are commonly used in artificial intelligence (AI) and game theory to solve problems related to game-playing, such as finding the best move in complex games like chess, Tictactoe, connect4 etc, where each player tries to maximize their own score and minimize their opponent's score.

Minimax was first proposed by John von Neumann in the 1920s as a way to solve two-player zero-sum games such as chess, checkers, and Go. The algorithm was later refined by other researchers, including John Nash, who introduced the concept of Nash equilibrium in game theory.

ABP was introduced by John McCarthy and his colleagues in the late 1950s as a way to improve the efficiency of the minimax algorithm by reducing the number of nodes that need to be evaluated. The algorithm was inspired by ideas from the minimax algorithm and the principle of branch-and-bound in optimization[^2].

This paper will first provide a detailed analysis of these two algorithms through time and space complexity. Then, it is going to analyze the runtime performance of the minimax algorithm and the abp algorithm through implementing these two algorithms to a game called connect4. Due to the intensity of time, the game is a depth-limited version of connect4 borrowed the GUI interface from Pei Xu(peix@g.clemson.edu), but the algorithms are implemented as individual efforts. The paper is seeking to compare the performance of each of these two algorithms by initiating two players, one is the maximizing player while the other is the minimizing player. The user has a choice to choose whether it is minimax vs. minimax or minimax vs. abp. The user also has an option to choose play against the minimax or abp AI player. The runtime analysis will be presented by line chart, and the results of the game play will be shown in graphics. Language analysis will be presented.

[^1]: "Alpha-Beta pruning": https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#:~:text=Alpha%E2%80%93beta%20pruning%20is%20a,Connect%204%2C%20etc
[^2]: "Russell, S. J., & Norvig, P. (2010). Artificial intelligence: A modern approach (3rd ed.). Prentice Hall. p193-195": https://scholar.alaqsa.edu.ps/9195/1/Artificial%20Intelligence%20A%20Modern%20Approach%20%283rd%20Edition%29.pdf%20%28%20PDFDrive%20%29.pdf


## Analysis of Algorithm
In Minimax, the maximizing player's goal is to select a move that maximize the function whereas the minimizer is selecting a move that minimizes the function. Therefore the time complexity of Minimax is $O(b^m)$ and space complexity is $O(bm)$ where b is the number of legal moves at each point, and m is the maximum depth of the tree. 

While in ABP, as it is optimizing Minimax through pruning out the nodes whose values fall outside of the bound alpha and beta, it should be more efficient than Minimax. However, in the worst case, where no node has been pruned out, the time complexity is the same with Minimax. But in the optimal case, each node will examine 2b-1 grandchildren to decide on its value. In the worst case, the node would examine $b^2$ grandchildren[^3]. The number of leaf node positions evaluated is about $O(b*1*b*1*...*b)$ for odd depth and $O(b*1*b*1*...*1)$ for even depth. This is because for every maximizer who plays first, all their moves has to be evaluated to find the best one, but for the minimizer, only the best move needs to be evaluated. Thereefore, in the optimal case, the time complexity of ABP is $O(b^(d/2))$. While this indicates that given the same amount of time, ABP can search twice as deep as Minimax, it does not affect the space complexity, so the space complexity of ABP is the same as Minimax, that is, $O(bm)$.

![minimax_example]

(Source [Minimax](https://en.wikipedia.org/wiki/Minimax#:~:text=Minimax%20(sometimes%20MinMax%2C%20MM%20or,to%20maximize%20the%20minimum%20gain.))


The above illustrates how the Minimax algorithm works. The algorithm uses DFS, it starts from the bottom and evaluates the maximum and minimum values of the leaf nodes alternately until it reaches the root node.

![abp_example]

(Source: [ABP](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning))

This diagram shows how the ABP algorithm works. The gray part does not need to be evaluated, as they cannot lead to a change in the final result. 


[^3]: https://cis.temple.edu/~vasilis/Courses/CIS603/Lectures/l7.html



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


<!-- auto references -->
[minimax_example]: minimax_example.png
[abp_example]: abp_example.png
