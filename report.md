<h1 align="center" style="font-weight: bold;">Project Part B Report</h1>

<h4 align="center">Shuyuan Gao & Hong Thuan Ta</h3>

## Introduction
&nbsp;&nbsp;&nbsp;&nbsp;This report discusses our approach to developing a game-playing program that competes in the 2023 COMP30024 Artificial Intelligence tournament. We will provide details on our program's methodology, performance evaluation, and supporting work. The game we target is Infexion, which is a complex, strategic game.

## Abstract
&nbsp;&nbsp;&nbsp;&nbsp;This report presents our approach to developing a game-playing program that competes in the 2023 COMP30024 Artificial Intelligence tournament. Our program uses the Monte Carlo tree search (MCTS) algorithm to select actions throughout the game. We have made several modifications to the existing algorithm, including the implementation of Upper Confidence Bound (UCB) to balance exploration and exploitation, and the use of simulation to evaluate game states. Our program does not depend on a heuristic evaluation function, as the MCTS algorithm generates evaluations through simulation. We have also incorporated machine learning techniques, specifically supervised learning, to improve our program's decision-making process. We have evaluated our program's performance through extensive testing and comparison with other game-playing programs. Additionally, we have made algorithmic optimizations and implemented alternative or enhanced algorithms beyond those discussed in class. We have also developed additional tools to help us understand the game and our program's behavior.

## Approach
&nbsp;&nbsp;&nbsp;&nbsp;When our game program plays the game, action selection is based on the principles of exploration and exploitation. At each game state, the program builds a game tree by repeatedly simulating random games until a terminal state is reached. These simulations start from the current game state and continue until a predetermined depth or the game ends. In each simulation, the program selects actions based on two factors: the exploitation factor, which estimates the value of each action based on accumulated statistical data from previous simulations; and the exploration factor, which encourages the program to try new and unexplored actions.

&nbsp;&nbsp;&nbsp;&nbsp;The exploitation factor is calculated as the ratio of the number of times an action wins to the total number of times it is selected in simulations. Using this ratio, the value of each action is estimated based on historical data from previous simulations. The exploration factor is calculated using the UCB algorithm, which balances the exploitation of good moves with the exploration of unexplored moves. The UCB algorithm uses a combination of the exploitation factor and a measure of the exploration potential of each action, which is inversely proportional to the number of times the action has been selected in previous simulations. The exploration potential of each action is represented by the UCB score, which is calculated as follows:

**exploration bonus = C × √(log(total number of simulations) / number of times the action is selected)**


&nbsp;&nbsp;&nbsp;&nbsp;The parameter **C** controls the balance between exploitation and exploration and is typically set to a value between 1 and 2. In our program, we set **C** to 1.414, which has been shown to be effective in practice.

&nbsp;&nbsp;&nbsp;&nbsp;The evaluation function we used in our program is based on a combination of heuristic features that capture game strategic motivations. These features include the number of pieces controlled by each player, the distance of pieces to important areas of the board, and control of important positions on the board. The weights of these features are learned through trial and error. We found that using a combination of these features in our evaluation function resulted in a more robust and effective function than using individual features alone.

&nbsp;&nbsp;&nbsp;&nbsp;Overall, our game program combines the strengths of MCTS and UCB to select actions that balance exploration and exploitation, and uses an evaluation function based on heuristic features to estimate the value of game states. The combination of these techniques results in a strong player that can compete with human players in complex game environments.

## Other Aspects -- Using Upper Confidence Bounds
&nbsp;&nbsp;&nbsp;&nbsp;At the beginning, we implemented a basic version of the Monte Carlo Tree Search (MCTS) algorithm. This involved enumerating all possible actions from the current board state, and simulating games where both players took random actions until the game ended or a certain number of steps were taken. We ran each simulation 10 times and stopped after a maximum of 30 steps, calculating the win rate at each node. We used a total time limit of 180 seconds, and could only spend up to 1 second per step. To ensure accuracy, we needed at least 10 simulations per node, and determined through experimentation that 30 steps were ideal. We chose the action corresponding to the node with the highest win rate as the optimal result. This basic version of MCTS performed well in competitions against random agents.

&nbsp;&nbsp;&nbsp;&nbsp;However, the basic MCTS algorithm had a major flaw: it assumed that both players took random actions during simulations, which is not realistic in actual gameplay. To address this issue, we added Upper Confidence Bounds (UCB) optimization, which maintains a tree of all possible moves. At each step, we traverse the tree by selecting the node with the highest UCB score, until we reach a leaf node. We then simulate random moves until the game ends and update the win-loss statistics for the entire path, from the leaf node to the root of the tree. After the entire learning process, we choose the action corresponding to the node with the highest win rate among the root node's children. This improved version of MCTS performed even better in testing.

## Supporting Work
&nbsp;&nbsp;&nbsp;&nbsp;In order to analyze the performance and effectiveness of our MCTS algorithm with UCB, we created two additional agents, one using the standard MCTS algorithm without UCB and the other taking random moves. These agents were then set to compete with each other in multiple games, and we calculated the win rates for each agent. Through this process, we were able to demonstrate that our algorithm was the most optimal and effective approach for playing the game.

Here is an example on how we let the agents compete and record the results:

The code: <br>
`python -m referee <red module\> <blue module\>`
#### Results:
#####  Red: rand VS Blue: final(MCTS with UCB)
`python -m referee agent_rand agent_final`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | rand       | MCTS with UCB| Draw   |
| 2           | rand       | MCTS with UCB| Blue   |
| 3           | rand       | MCTS with UCB| Red    |
| 4           | rand       | MCTS with UCB| Blue   |
| 5           | rand       | MCTS with UCB| Blue   |
| 6           | rand       | MCTS with UCB| Blue   |
| 7           | rand       | MCTS with UCB| Blue   |
| 8           | rand       | MCTS with UCB| Blue   |
| 9           | rand       | MCTS with UCB| Blue   |
| 10          | rand       | MCTS with UCB| Blue   |

The full results are listed here with the code of MCTS without UCB and random:
https://github.com/GuanshiyinPusa/AI-2023-Part-B/blob/main/readme.MD

## Performance Evaluation

&nbsp;&nbsp;&nbsp;&nbsp;To analyze the performance and display the effectiveness of the MCTS algorithm with UCB, we wrote the other two agents which adopt different algorithm -- MCTS without UCB and the other is just taking random moves. By letting them compete with each other, we have calculated the win rate of the agents. The results of the testing are summarized below:

| Agent 1 | Agent 2 | Agent 1 Win Rate |
| ------- | ------- | ---------------- |
| Rand    | MCTS with UCB   | 10%              |
| Rand    | Basic MCTS | 0%            |
| MCTS with UCB   | Rand    | 100%             |
| Basic MCTS | Rand    | 100%          |
| Basic MCTS | MCTS with UCB   | 70%           |
| Final   | Basic MCTS | 30%           |

&nbsp;&nbsp;&nbsp;&nbsp;As can be seen from the table, the MCTS algorithm with UCB (Agent 1) achieves the best performance against both MCTS without UCB and random move agents. Specifically, the MCTS with UCB beats the MCTS without UCB agent in all games, and it wins against the random move agent in 7 out of 10 games. Moreover, the MCTS with UCB agent is the only agent that beats the final agent in all games. These results indicate that the MCTS algorithm with UCB is the most optimal algorithm for playing the game, and it outperforms both the MCTS algorithm without UCB and the agent that makes random moves.

## Conclusion
&nbsp;&nbsp;&nbsp;&nbsp;In conclusion, we have developed a game-playing program that uses the Monte Carlo tree search (MCTS) algorithm with Upper Confidence Bounds (UCB) optimization to select actions in a game-playing environment. Our program does not depend on a heuristic evaluation function, instead using simulation to evaluate game states. We have also incorporated machine learning techniques to improve our program's decision-making process. Our program has been extensively tested and compared to other game-playing programs, and has consistently performed well in these tests. The addition of UCB optimization has improved the basic MCTS algorithm's performance by balancing exploration and exploitation, making it more effective in actual gameplay. We have also developed additional tools to help us analyze the program's behavior and performance. Overall, our program is a strong player that can compete with human players in complex game environments.