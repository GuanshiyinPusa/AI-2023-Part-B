GSY is stronger
final is GPT

`python -m referee agent_basic_MCTS agent_stronger` ---- GSY 50%
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | basic      | GSY         | blue   |
| 2           | basic      | GSY         | red    |
| 3           | basic      | GSY         | blue   |
| 4           | basic      | GSY         | red    |
| 5           | basic      | GSY         | blue   |
| 6           | basic      | GSY         | red    |
| 7           | basic      | GSY         | blue   |
| 8           | basic      | GSY         | blue   |
| 9           | basic      | GSY         | red    |
| 10          | basic      | GSY         | red    |

`python -m referee agent_basic_MCTS agent_final`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | basic      | GPT         | blue   |
| 2           | basic      | GPT         | blue   |
| 3           | basic      | GPT         | red    |
| 4           | basic      | GPT         | red    |
| 5           | basic      | GPT         | red    |
| 6           | basic      | GPT         |    |
| 7           | basic      | GPT         |    |
| 8           | basic      | GPT         |    |
| 9           | basic      | GPT         |    |
| 10          | basic      | GPT         |    |

`python3 -m referee agent_stronger agent_final`     ---- GSY 80%
| Game Number | Red Player | Blue Player | Winner |
| 1           | GSY        | GPT         | blue   |
| 2           | GSY        | GPT         | blue   |
| 3           | GSY        | GPT         | red    |
| 4           | GSY        | GPT         | red    |
| 5           | GSY        | GPT         | red    |
| 6           | GSY        | GPT         | red    |
| 7           | GSY        | GPT         | red    |
| 8           | GSY        | GPT         | red    |
| 9           | GSY        | GPT         | red    |
| 10          | GSY        | GPT         | red    |

`python -m referee agent_final agent_stronger `
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | GPT        | GSY         | red    |
| 2           | GPT        | GSY         | red    |
| 3           | GPT        | GSY         | red    |
| 4           | GPT        | GSY         | red    |
| 5           | GPT        | GSY         | red    |
| 6           | GPT        | GSY         | red    |
| 7           | GPT        | GSY         |    |
| 8           | GPT        | GSY         |    |
| 9           | GPT        | GSY         |    |
| 10          | GPT        | GSY         |    |

