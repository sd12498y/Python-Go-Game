# Python-Go-Game

## Usage
* Type in command line the following

### Play as black player against the computer
```Python
python main.py human computer
```

### Play as white player against the computer
```Python
python main.py computer white
```

### Let SQagent and the computer playing themselves with SQagent playing the black with n rounds
```Python
python main.py SQ computer n
```

### Let SQagent and the computer playing themselves with SQagent playing the white with n rounds
```Python
python main.py computer SQ n
```

## Methodologies:
### 1. Minimax search
### 2. Alpha-beta pruning (default_depth = 5)

## Evaluation function:
The current adopted strategy is positional strategy, with a score assigned on each of the position in the game board. Illustration as in the following graph.
The score of other positions are just the symmetries of the given score.
The complete distribution is (99,-8,8,6,6,8,-8,99,-8,-24,-4,-3,-3,-4,-24,-8,8,-4,7,4,4,7,-4,8,6,-3,4,0,0,4,-3,6,6,-3,4,0,0,4,-3,6,8,-4,7,4,4,7,-4,8,-8,-24,-4,-3,-3,-4,-24,-8,99,-8,8,6,6,8,-8,99)
Adding up the score where the player’s discs are occupying can get the sum of a player/
The evaluation function returns the difference between the sum of the player and the sum of opponent.

## Self-learning:
Q-learing (SQ agent)
Scores = Win = 7; Tie = 0; Lose = -7
Initial Learning rate(alpha) = 1
Discount rate = 1

Thanks to Yu, Ng, Josephine and Anna, who are a group of HKU CS graduates, I have obtained a large amount of data from http://i.cs.hku.hk/~kpchan/Othello/TrainingSet.html.  The data collected by them are more than suitable for me to implement reinforcement learning. I have transformed each game in my format, (player, col, row, win/lose) for the learning of the Q value of each (state, action) pair.

The score of each (state, action) pair is stored in “book.txt”
Whenever the game is started, a class object called book will get all the data from “book.txt”, and stored all information in dictionaries structure
Add and update records in the Book object
Save the dictionary into the book.txt by completely rewriting

For each (state, action) pair, the value is initialized with Infinity to encourage the agent to explore it in real game. As a result, the corresponding Q value will be largely dropped after the game has finished.

