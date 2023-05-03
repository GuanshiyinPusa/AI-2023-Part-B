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
| 4           | rand       | basic       |        |
| 5           | rand       | basic       |        |
| 6           | rand       | basic       |        |
| 7           | rand       | basic       |        |
| 8           | rand       | basic       |        |
| 9           | rand       | basic       |        |
| 10          | rand       | basic       |        |

#### Red: basic VS Blue: rand
`python -m referee agent_basic_MCTS agent_rand`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | basic      | rand        | RED    |
| 2           | basic      | rand        | RED    |
| 3           | basic      | rand        | RED    |
| 4           | basic      | rand        | RED    |
| 5           | basic      | rand        | RED    |
| 6           | basic      | rand        | RED    |
| 7           | basic      | rand        | RED    |
| 8           | basic      | rand        | RED    |
| 9           | basic      | rand        | RED    |
| 10          | basic      | rand        | RED    |

#### Red: basic VS Blue: final
`python -m referee agent_basic_MCTS agent_final`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | basic      | final       | RED    |
| 2           | basic      | final       | RED    |
| 3           | basic      | final       | BLUE   |
| 4           | basic      | final       | BLUE   |
| 5           | basic      | final       | RED    |
| 6           | basic      | final       | RED    |
| 7           | basic      | final       | RED    |
| 8           | basic      | final       | BLUE   |
| 9           | basic      | final       | RED    |
| 10          | basic      | final       | RED    |

#### Red: final VS Blue: basic
`python -m referee agent_final agent_basic_MCTS`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | final      | basic       | RED    |
| 2           | final      | basic       | RED    |
| 3           | final      | basic       | BLUE   |
| 4           | final      | basic       | BLUE   |
| 5           | final      | basic       | RED    |
| 6           | final      | basic       | BLUE   |
| 7           | final      | basic       | RED    |
| 8           | final      | basic       | RED    |
| 9           | final      | basic       | BLUE   |
| 10          | final      | basic       | RED    |

