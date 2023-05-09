#### three command for testing:
<br>
`python -m referee agent agent`
<br>
`python -m referee agent agent_rand`
<br>
`python -m referee agent agent_basic_MCTS`

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
| 1           | basic      | final       | Red   |
| 2           | basic      | final       | Blue  |
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

