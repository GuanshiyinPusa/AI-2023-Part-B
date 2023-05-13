#### three command for testing:
<br>
`python -m referee agent_final agent`
<br>
`python -m referee agent_final agent_rand`
<br>
`python -m referee agent_final agent_basic_MCTS`
<br>
`python -m referee agent_v1 agent_final`
<br>
`python -m referee agent_v2 agent_final`
<br>
`python -m referee agent_v3 agent_final`
#### Note:<br>
python -m referee <red module\> <blue module\>
<br>
**What i want to do is that I should record the win and lose between:**
- rand VS final
- rand VS basic_MCTS
- final VS basic_MCTS
<br>
#### results:
<br>

#### Red: rand VS Blue: final
`python -m referee agent_rand agent_final`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | rand       | final       | Draw   |
| 2           | rand       | final       | Blue   |
| 3           | rand       | final       | Red    |
| 4           | rand       | final       | Blue   |
| 5           | rand       | final       | Blue   |
| 6           | rand       | final       | Blue   |
| 7           | rand       | final       | Blue   |
| 8           | rand       | final       | Blue   |
| 9           | rand       | final       | Blue   |
| 10          | rand       | final       | Blue   |

#### Red: final VS Blue: rand
`python -m referee agent_final agent_rand`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | final      | rand        | Red    |
| 2           | final      | rand        | Red    |
| 3           | final      | rand        | Red    |
| 4           | final      | rand        | Red    |
| 5           | final      | rand        | Red    |
| 6           | final      | rand        | Red    |
| 7           | final      | rand        | Red    |
| 8           | final      | rand        | Red    |
| 9           | final      | rand        | Red    |
| 10          | final      | rand        | Red    |

#### Red: rand VS Blue: basic
`python -m referee agent_rand agent_basic_MCTS`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | rand       | basic       | Blue   |
| 2           | rand       | basic       | Blue   |
| 3           | rand       | basic       | Blue   |
| 4           | rand       | basic       | Blue   |
| 5           | rand       | basic       | Blue   |
| 6           | rand       | basic       | Blue   |
| 7           | rand       | basic       | Blue   |
| 8           | rand       | basic       | Blue   |
| 9           | rand       | basic       | Blue   |
| 10          | rand       | basic       | Blue   |

#### Red: basic VS Blue: rand
`python -m referee agent_basic_MCTS agent_rand`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | basic      | rand        | Red    |
| 2           | basic      | rand        | Red    |
| 3           | basic      | rand        | Red    |
| 4           | basic      | rand        | Red    |
| 5           | basic      | rand        | Red    |
| 6           | basic      | rand        | Red    |
| 7           | basic      | rand        | Red    |
| 8           | basic      | rand        | Red    |
| 9           | basic      | rand        | Red    |
| 10          | basic      | rand        | Red    |

#### Red: basic VS Blue: final
`python -m referee agent_basic_MCTS agent_final`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | basic      | final       | Red    |
| 2           | basic      | final       | Blue   |
| 3           | basic      | final       | Red    |
| 4           | basic      | final       | Red    |
| 5           | basic      | final       | Red    |
| 6           | basic      | final       | Red    |
| 7           | basic      | final       | Blue   |
| 8           | basic      | final       | Blue   |
| 9           | basic      | final       | Red    |
| 10          | basic      | final       | Red    |

#### Red: final VS Blue: basic
`python -m referee agent_final agent_basic_MCTS`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | final      | basic       | Red    |
| 2           | final      | basic       | Red    |
| 3           | final      | basic       | Red    |
| 4           | final      | basic       | Red    |
| 5           | final      | basic       | Red    |
| 6           | final      | basic       | Red    |
| 7           | final      | basic       | Red    |
| 8           | final      | basic       | Blue   |
| 9           | final      | basic       | Red    |
| 10          | final      | basic       | Red    |

Time analysis:
| command                                             | user    | system | total   |
|-----------------------------------------------------|---------|--------|---------|
| time python3 -m referee agent_rand agent_final      | 167.00s | 1.19s  | 3:06.85 |
| time python3 -m referee agent_rand agent_basic_MCTS | 359.34s | 1.72s  | 6:13.22 |
| time python3 -m referee agent_rand agent_v1         | 146.67s | 1.81s  | 3:10.13 |
| time python3 -m referee agent_rand agent_v2         | 173.73s | 0.84s  | 3:04.36 |
| time python3 -m referee agent_rand agent_v3         | 180.92s | 0.60s  | 3:0327  |   

| command                                             | user    | system | total   |
|-----------------------------------------------------|---------|--------|---------|
| time python3 -m referee agent_final agent_rand      | 181.95s | 0.67s  | 3:05.86 |
| time python3 -m referee agent_basic_MCTS agent_rand | 361.41s | 0.93s  | 8:40.83 |
| time python3 -m referee agent_v1 agent_rand         | 182.89s | 0.61s  | 3:05.46 |
| time python3 -m referee agent_v2 agent_rand         | 180.49s | 0.76s  | 3:04.67 |
| time python3 -m referee agent_v3 agent_rand         | 181.94s | 0.65s  | 3:04.49 |



