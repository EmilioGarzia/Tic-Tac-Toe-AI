<!-- toc start: 3 [do not erase this comment] -->
**Table of contents**
- [Tic-Tac-Toe: AI](#tic-tac-toe-ai)
	- [Features](#features)
		- [AI Algorithms](#ai-algorithms)
		- [Uncertainty of the AI](#uncertainty-of-the-ai)
		- [Game modes](#game-modes)
	- [How to Run](#how-to-run)
- [Clone the repo](#clone-the-repo)
- [Open directory project](#open-directory-project)
- [Launch the main script](#launch-the-main-script)
	- [How to manage the smart level](#how-to-manage-the-smart-level)
	- [Main class implemented entities](#main-class-implemented-entities)
		- [Attributes](#attributes)
		- [Costants](#costants)
		- [Methods](#methods)
	- [Author](#author)
<!-- toc end [do not erase this comment] -->

# Tic-Tac-Toe: AI

This project is an educational implementation of the Tic-Tac-Toe game, featuring artificial intelligence powered by the **Minimax** and **Alpha-Beta Pruning** algorithms. It is designed to demonstrate how these algorithms can be applied to solve decision-making problems in games.

## Features

### AI Algorithms
- **Minimax**: A brute-force algorithm that explores all possible moves to determine the optimal strategy.
    - $\text{Time Complexity} = O\left(b^d\right)$
    - $\text{Space Complexity} = O(bd)$
- **Alpha-Beta Pruning**: An optimized version of Minimax that reduces the number of nodes evaluated in the search tree.
    - $\text{Time Complexity} = O\left(b^{\frac{d}{2}}\right)$
    - $\text{Space Complexity} = O(bd)$

ℹ: $b$ is number of legal moves in that moment, $d$ is the max depth of the decision tree

### Uncertainty of the AI
- **High**: Optimal moves are always chosen.
- **Medium**: A mix of optimal and suboptimal moves.
- **Low**: Randomized suboptimal moves to simulate uncertainty.

⚠️: If you use **Alpha-Beta Pruning** as CPU algorithm, the choice of smart level is quite useless, because the structure of this algorithm prune many non optimal branches, this leads to choose the best action, independently from your fixed smart level

### Game modes
- **CPU vs CPU**: Watch two AI players compete.
- **Player vs CPU**: Play against the AI.
- **Player vs Player**: Play against another human.
- **Game Insights**: Displays the result of the game, including the winner, winning coordinates, and game duration.

## How to Run
```bash
# Clone the repo
git clone https://github.com/EmilioGarzia/Tic-Tac-Toe-AI
# Open directory project
cd Tic-Tac-Toe-AI
# Launch the main script
python main.py
```

## How to manage the smart level

You can handle the smart level of the AI algorithm, to do this, you have to set the top $n$ best actions collected during the algorithm recursion, so change the values into `__top_n_actions__()` method. I suggest you to avoid to change the `HIGH` level, otherwise, you loose the optimality of the algorithm. Below an example of setting.

```python
def __top_n_actions__(self, actions, smart_level):
        if smart_level == self.HIGH:
            top_n = 1  # optimal choice
        elif smart_level == self.MEDIUM:
            top_n = 5  # MEDIUM smart level
        elif smart_level == self.LOW:
            top_n = 10 # LOW smart level
        else:
            top_n = 1
        
        top_n_actions = actions[:top_n]
        return random.choice(top_n_actions)[1]
```

> ⚠️: Higher values denotes lower smart levels, and viceversa

## Main class implemented entities
The core of the program is contained inside the class `TicTacToe`, below I've reported all definition of this class.

### Attributes
- `player1_symbol`: the char which represent the player one on the game's field 
- `player2_symbol`: the char which represent the player two on the game's field 
- `field_state`: a 2D matrix (built using `list()`) which contains the current state of the game's field
- `moves`: total amount of done moves in the current game
- `elapsed_time`: the game's duration at the end of a game (in milliseconds) 

### Costants
- `PLAYER1`: represent player one in the game
- `PLAYER2`: represent player two in the game
- `EMPTY_CELL`: denote an empty cell on the game's field
- `DRAW`: denote a tie game
- `VERTICAL_WIN`: denote a game ended with a win occurs on vertical column of the field
- `HORIZONTAL_WIN`: denote a game ended with a win occurs on horizontal row of the field
- `MAIN_DIAG_WIN`: denote a game ended with a win occurs on the main diagonal
- `SECOND_DIAG_WIN`: denote a game ended with a win occurs on the second diagonal
- `MINIMAX`: indicates that the AI uses MINIMAX algorithm to takes actions
- `ALPHA_BETA_PRUNING`: indicates that the AI uses ALPHA-BETA PRUNING algorithm to takes actions
- `LOW`: indicates that the smart level of the AI algorithm is low
- `MEDIUM`: indicates that the smart level of the AI algorithm is medium
- `HIGH`: indicates that the smart level of the AI algorithm is high (always the optimal action)

### Methods

- `player()`: Returns the current player (`PLAYER1` or `PLAYER2`) based on the move count.
- `actions()`: Returns a list of all valid moves (i.e., empty cells) on the board.
- `result(action)`: Applies a valid move to the board and updates the move count.
- `result_simulated(action)`: Simulates a move and returns a new game state without modifying the original.
- `minimax(smart_level=302)`: Executes the Minimax algorithm with a configurable difficulty level. Returns the chosen move.
- `alpha_beta_pruning(smart_level=302)`: An optimized version of Minimax with alpha-beta pruning for better performance.
- `__top_n_actions__(actions, smart_level)`: Internal method that randomly selects one of the top actions based on the AI smart level (HIGH, MEDIUM, LOW).
- `terminal()`: Checks if the game has ended. Returns a tuple with end status, win type, and winning coordinates.
- `utility()`: Returns the numerical result of the game: `PLAYER1`, `PLAYER2`, or `DRAW`.
- `print_mapping()`: Displays the board's coordinate mapping to assist the player in choosing cell positions.
- `print_field()`: Prints the current state of the game board in a readable format.
- `restart()`: Resets the game to the initial state.
- `set_player_symbol(player_number, symbol)`: Allows customization of the players’ symbols.
- `cpu_vs_cpu_AI_simulation(smart_level=302, print_moves=False, algorithm=200)`: Simulates a game between two AIs using either Minimax or Alpha-Beta. Measures execution time.
- `player_vs_cpu(smart_level=302, player1=True)`: Allows a human player to play against the CPU. Player can choose to go first or second.
- `player_vs_player()`: Enables a human vs human game session.
- `print_insights(stop_term=True, winner_coords=True, elapsed_time=True)`: Prints game statistics including win type, winner, winning coordinates, and duration.
- `__checkMonovaluesArray__(vector, verbose=False)`: Static helper method to verify if all elements in a list are the same (used for win conditions).

## Author
Emilio Garzia, 2025
