daixie is stronger
final is GPT

`python -m referee agent_basic_MCTS agent_stronger`
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | basic      | daixie      | blue   |
| 2           | basic      | daixie      | red    |
| 3           | basic      | daixie      | blue   |
| 4           | basic      | daixie      | red    |
| 5           | basic      | daixie      | blue   |
| 6           | basic      | daixie      | red    |
| 7           | basic      | daixie      | blue   |
| 8           | basic      | daixie      | blue   |
| 9           | basic      | daixie      |    |
| 10          | basic      | daixie      |    |

`python -m referee agent_stronger agent_final`
| Game Number | Red Player | Blue Player | Winner |
| 1           | daixie     | GPT         | blue   |
| 2           | daixie     | GPT         | blue   |
| 3           | daixie     | GPT         | red    |
| 4           | daixie     | GPT         | red    |
| 5           | daixie     | GPT         | red    |
| 6           | daixie     | GPT         | red    |
| 7           | daixie     | GPT         | red    |
| 8           | daixie     | GPT         | red    |
| 9           | daixie     | GPT         | red    |
| 10          | daixie     | GPT         |    |

`python -m referee agent_final agent_stronger `
| Game Number | Red Player | Blue Player | Winner |
|-------------|------------|-------------|--------|
| 1           | basic      | GPT         | blue   |
| 2           | GPT        | daixie      | red    |
| 3           | GPT        | daixie      | red    |
| 4           | GPT        | daixie      |    |
| 5           | GPT        | daixie      |    |
| 6           | GPT        | daixie      |    |
| 7           | GPT        | daixie      |    |
| 8           | GPT        | daixie      |    |
| 9           | GPT        | daixie      |    |
| 10          | GPT        | daixie      |    |

