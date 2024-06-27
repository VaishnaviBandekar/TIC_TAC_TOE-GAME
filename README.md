# TIC_TAC_TOE-GAME

This is a simple Tic Tac Toe game implemented in Python using the tkinter library for the graphical user interface. The game includes an AI opponent using the Minimax algorithm to provide a challenging gameplay experience.

## Features

- Player vs. AI
- Interactive graphical user interface
- Minimax algorithm for AI decision-making
- Option to restart the game

## Requirements

- Python 3.x
- tkinter library (usually included with Python)

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the directory where you cloned the repository.
3. Run the following command to start the game:

```sh
python tictactoe.py
Gameplay
The game starts with an empty 3x3 board.
The player makes the first move by clicking on an empty cell.
The AI opponent (playing as "O") makes its move using the Minimax algorithm.
The game continues until there is a winner or the board is full (resulting in a tie).
Click the "Restart Game" button to start a new game.
Code Overview
The main components of the code are:

TicTacToe: The main class that sets up the game window and handles the game logic.
create_board(): Creates the game board with buttons for each cell.
reset_game(): Resets the game to the initial state.
player_move(idx): Handles the player's move and checks for a winner or tie.
computer_move(): Executes the AI's move using the Minimax algorithm.
check_winner(player): Checks if the specified player has won the game.
minimax(depth, is_maximizing): The Minimax algorithm implementation for AI decision-making.
get_best_move(): Determines the best move for the AI.

## Screenshots


### AI WINS
![AI Wins](Screenshots/O_WIN_RESULT.png)

### GAME TIE
![Game Tie](screenshots/TIE_RESULT.png)


License
This project is licensed under the MIT License. See the LICENSE file for details.


Contact
For any inquiries or suggestions, please contact vaishnavi.b1418@gmail.com.
