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


(Source: [Minimax](https://en.wikipedia.org/wiki/Minimax#:~:text=Minimax%20(sometimes%20MinMax%2C%20MM%20or,to%20maximize%20the%20minimum%20gain.)))


The above illustrates how the Minimax algorithm works. The algorithm uses DFS, it starts from the bottom and evaluates the maximum and minimum values of the leaf nodes alternately until it reaches the root node.

![abp_example]

(Source: [ABP](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning))

This diagram shows how the ABP algorithm works. The gray part does not need to be evaluated, as they cannot lead to a change in the final result. 


[^3]: https://cis.temple.edu/~vasilis/Courses/CIS603/Lectures/l7.html



## Empirical Analysis
According to the time complexity analysis and the algorithm analysis, ABP shoule run faster than Minimax for the same depth, and the search results are the same as the ABP would end searching if the optimal results are found.

I ran my game, for each depth, the game results are the same for each algorithm.

![result1]

![result2]

![result3]

![result4]

![result5]

The score are the same for all algorithms.

```text
depth limit = 1:
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 2, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0]
[0, 0, 2, 2, 2, 0, 0]
[0, 1, 1, 1, 1, 0, 0]
```

```text
depth limit = 2:
[2, 2, 1, 1, 0, 1, 0]
[1, 1, 2, 2, 0, 2, 1]
[1, 2, 1, 1, 1, 1, 2]
[2, 1, 2, 2, 2, 1, 1]
[1, 2, 1, 1, 1, 2, 2]
[2, 1, 2, 2, 2, 1, 2]
```

```text
depth limit = 3:
[0, 2, 2, 1, 0, 2, 0]
[0, 1, 2, 2, 0, 2, 2]
[0, 1, 2, 2, 0, 1, 1]
[0, 2, 1, 1, 0, 1, 2]
[0, 1, 2, 2, 1, 1, 1]
[0, 2, 1, 1, 1, 2, 1]
```

```text
depth limit = 4:
[1, 2, 2, 2, 1, 2, 2]
[2, 1, 1, 1, 2, 1, 1]
[2, 2, 2, 1, 1, 1, 2]
[1, 1, 1, 2, 2, 2, 1]
[2, 2, 2, 1, 1, 1, 2]
[2, 1, 1, 1, 2, 2, 1]
```

```text
depth limit = 5: 
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0, 0]
[0, 0, 2, 2, 1, 1, 0]
[0, 0, 1, 2, 2, 2, 0]
[0, 0, 2, 1, 1, 2, 0]
[0, 2, 1, 1, 1, 2, 2]
```
The above demonstrated that Minimax and ABP are essentially having the same function, therefore leads to same game results.

However, the runtime of each algorithm in different depth is illustrated below.

| Depth |  Minimax /s  | ABP /s | 
| :-- | :-- |  :-- |
| 1 | 0.0009229183197021484 | 0.0006542205810546875  |
| 2| 0.0060498714447021484 | 0.0033948421478271484 |
| 3 | 0.04245901107788086 | 0.016826868057250977 |
| 4 | 0.28708410263061523 | 0.06319499015808105 |
| 5 | 1.9482190608978271 | 0.28275012969970703|

As the depth becomes deeper, the runtime difference becomes more significant. The table here probably does not display this information at one glance, but it is clear when demonstrated by line charts.

![Minimax_runtime]

![ABP_runtime]

As can be seen from the difference between the scale of Y-axis from each diagram above, the time difference is significant.

However, it also means that in terms of which algorithm is preferred, the number of legal moves is important, if the number of legal moves is small, then minimax can be better as it is easier to develop, and space complexity are the same for both.

![Comparison_runtime]

This comparison diagram further illustrates the time complexity of Minimax and ABP respectively.

Overall, the analysis supports the theoretical understanding of Minimax and ABP and their respective time complexities.



## Implementations
I used Python to implement Minimax and ABP algorithms by developing a connect4 game. I started with developing the pseudocode of both. 

First, the programa terminates when the depth reaches zero or the node is the end node. If it is the maximizer, the value will be set at negative infinity, and then for each leaf node, the value will equal to the larger value of the initial value and the child's current value. This is where the recursion occurs. For the minimizer, the initial value will be set to positive infinity, and the child's current value will equal to the smaller value of the initial value and the child's current value by calling the minimax function.

Therefore, the pseudocode looks like:
```text
function minimax(node, depth, maximizer) {
    if depth == 0 or the node is the end node:
        return the value of the node
    else if the player is the maximizer:
        value = negative infinity
        for each leaf node:
            value = max(value, minimax(this leaf node, depth, False))
        return value
    else if this is the minimizer:
        value = positive infinity
        for each leaf node:
            value = min(value, minimax(this leaf node, depth, True))
        return value
}
```

For ABP, since this algorithm is optimizing Minimax through cutting off the unreachable part through comparing the values with alpha and beta, there needs to be two more parameters.

```text
function abp(depth, alpha, beta, node, maximizer) {
    if depth == 0 or the node is the end node:
        return the value of the node
    else if the player is the maximizer:
        value = negative infinity
        for each leaf node:
            value = max(value, abp(child, depth − 1, alpha, beta, FALSE))
            alpha = max(alpha, value)
            if (value > beta):
                break // this is where the cutoff happens
        return value
    else if this is the minimizer:
        value = positive infinity
        for each leaf node:
            value = min(value, abp(child, depth − 1, alpha, beta, TRUE))
            beta = min(value, beta)
            if (value < alpha):
                break // cutoff
}
```
When I implementing these to the connect4 game program, there needs to be a few changes as they should bear the function to place the chess onto the board and calculate the score. In addition, the program does not have to caculate the player's score, but also the opponent's score. Therefore, although the function uses Minimax and ABP, there are further development changes made to serve the gaming functionality.

The game is represented by the Board instance, and each player is identified as either PLAYER1 or PLAYER2. The evaluate function takes a player and a board instance as input and returns a score that represents the advantage of the player on the board. It computes the score for each 4-slot segment of the board and sums them up using a weighted scheme, where each score is multiplied by a weight depending on its length. The resulting score is the difference between the player's score and the adversary's score, where the adversary is the other player on the board.

The minimax function uses recursion to evaluate all possible moves that can be made on the game board. The algorithm works by assuming that both players will play optimally, and it selects the best move based on the score returned by the evaluation function. If the current player is maximizing, the function chooses the move with the highest score, and if the current player is minimizing, the function chooses the move with the lowest score. The evaluate function is used to determine the score for each move.

The alphabeta function is an optimization of the minimax algorithm, which prunes branches of the search tree that are not worth exploring. It does this by keeping track of two values alpha and beta, which represent the maximum score achievable by the maximizing player and the minimum score achievable by the minimizing player, respectively. If the algorithm determines that a branch cannot lead to a better outcome than the current best move, it prunes that branch and moves on to the next branch.

The player and board parameters represent the current state of the game, and the evaluate function is used to determine the score for each move.

I further developed a get_child_boards to serve the function of copying the current board, because I want the program to show every step taken, instead of displying the final board to the screen. It returns a list of tuples, where each tuple contains a column index and a new board state resulting from placing a piece in that column.

To test the outcome of the algorithms, due to the limitation of time, I borrowed the GUI interface (![app.py]) from Pei Xu (peix@g.clemson.edu). As displayed above in the Emperical Analysis, the user can select Minimax AI play against Minimax AI or Minimax AI against ABP AI. The user can also choose to play against Minimax AI or ABP AI. The outcome of all shows that they all have the same results, proving that Minimax and ABP are essentially sharing the same theory. I further wrote test script in ![test.py] to work out the efficiency of each algorithm and plot the results into line charts. I used the math library to get the value for alpha and beta, which are negative and positive infinity respectively. Then I imported the time library to time the runtime of each function. At last, I used the matplotlib library to plot the line charts and save them into the local repository.



## Summary
The results show that ABP outperformed Minimax in terms of runtime performance. As expected, ABP indeed pruned a lot of nodes that were not useful, thus saving some time. The line chart that shows the runtime performance of both algorithms clearly indicates that ABP is much faster than Minimax. This makes ABP a preferred choice when it comes to implementing AI for games that require a lot of computation.

However, the space complexity of ABP is still the same as Minimax, meaning that it requires the same amount of memory. This can be a limitation in games that require a lot of memory to store the game state, and in cases where the tree is too large to fit in memory. For future studies, I would consider using conducting a space complexity analysis of Minimax and ABP.

Additionally, the results showed that the performance of ABP and Minimax depends on the depth of the search tree. ABP performs better when the depth of the search tree is high, while Minimax performs better when the depth of the search tree is low. This can be attributed to the fact that ABP is more efficient in searching deeper trees, while Minimax is more efficient in searching shallower trees.

Furthermore, the results show that the performance of both algorithms depends on the number of legal moves available at each point. ABP performs better when the number of legal moves is high, while Minimax performs better when the number of legal moves is low. This is because ABP prunes more nodes when the number of legal moves is high, leading to less computational time, while Minimax performs better when the number of legal moves is low as it explores all possible moves.

In conclusion, ABP is an optimization of Minimax that prunes out nodes that are not useful, leading to less computational time. However, the space complexity of ABP is still the same as Minimax, and the performance of both algorithms depends on the depth of the search tree and the number of legal moves available at each point.

## References
1. Wikipedia contributors. (2021, March 28). Alpha–beta pruning. In Wikipedia, The Free Encyclopedia. Retrieved 20:30, April 12, 2023, from https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

2. Russell, S. J., & Norvig, P. (2010). Artificial intelligence: A modern approach (3rd ed.). Prentice Hall.

3. Temple University Department of Computer and Information Sciences. (n.d.). CIS 603: Artificial Intelligence. Retrieved April 12, 2023, from https://cis.temple.edu/~vasilis/Courses/CIS603/Lectures/l7.html

4. Wikipedia contributors. (2021, March 27). Minimax. In Wikipedia, The Free Encyclopedia. Retrieved 20:30, April 12, 2023, from https://en.wikipedia.org/wiki/Minimax

5. Browne, C. B., Powley, E., Whitehouse, D., Lucas, S. M., Cowling, P. I., Rohlfshagen, P., ... & Colton, S. (2012). A survey of Monte Carlo tree search methods. IEEE Transactions on Computational Intelligence and AI in games, 4(1), 1-43.

6. Minimax Algorithm in Game Theory | Set 4 (Alpha-Beta Pruning), from https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

7. Minimax Algorithm in Game Theory | Set 1 (Introduction), from https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/

8. Carnegie Mellon University Fundamentals of Game AI, from https://www.cs.cmu.edu/~112/notes/student-tp-guides/GameAI.pdf


<!-- auto references -->
[minimax_example]: minimax_example.png
[abp_example]: abp_example.png
[result1]: result1.png
[result2]: result2.png
[result3]: result3.png
[result4]: result4.png
[result5]: result5.png
[Minimax_runtime]: Minimax_runtime.png
[ABP_runtime]: ABP_runtime.png
[Comparison_runtime]: Comparison_runtime.png
[app.py]: /utils/app.py
[test.py]: /utils/test.py
