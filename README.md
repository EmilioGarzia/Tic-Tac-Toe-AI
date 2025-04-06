<!-- toc start: 3 [do not erase this comment] -->
**Table of contents**
- [Tic-Tac-Toe: AI](#tic-tac-toe-ai)
	- [Features](#features)
	- [How to Run](#how-to-run)
- [Clone the repo](#clone-the-repo)
- [Open directory project](#open-directory-project)
- [Launch the main script](#launch-the-main-script)
	- [Main class implemented entities](#main-class-implemented-entities)
		- [Attributes](#attributes)
		- [Costants](#costants)
		- [Methods](#methods)
	- [How to manage the smart level](#how-to-manage-the-smart-level)
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

### Uncertainly of the AI
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
> [todo]

## How to manage the smart level
> [todo]

## Author
Emilio Garzia, 2025
