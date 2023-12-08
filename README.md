# Memory Matching Game:
## Description
This Python program is a simple memory matching game created using the Turtle graphics library. Players flip over cards to find pairs of matching numbers. The game tracks which cards have been matched and ends when all pairs are found.


https://www.loom.com/share/f1ff9502343a48f9bfc9371c575f37b4?sid=0f05ffd9-7524-478f-ad9d-bca321958943

## Features
Dynamic Grid Layout: The game generates a grid of cards based on predefined settings.
Card Shuffling: Cards are shuffled at the beginning of each game to randomize their positions.
Interactive Gameplay: Players click on cards to flip them over and try to find matching pairs.
Game Over Detection: The game detects when all pairs have been matched and displays a game over message.

## Prerequisites
Python 3.x
Turtle Graphics Library (usually comes pre-installed with Python)
How to Run the Game
Ensure Python 3.x is installed on your system.
Copy the code into a .py file.
Run the file using Python.

## Gameplay Instructions
Click on a card to flip it over.
Try to find another card with the same number.
If a match is found, the cards will remain face up.
If a match is not found, the cards will flip back over after a short delay.
The game ends when all matches are found.


## Functions
init_game(): Initializes the game by creating and shuffling the cards.
draw_grid(): Draws the grid of face-down cards.
select_card(x, y): Handles card selection based on mouse clicks.
draw_card(position, value, face_down): Draws a single card.
reset_game(): Resets the game to start a new round.
check_match(): Checks if two selected cards are a match.
game_over(): Displays a game over message when all matches are found.
play_game(): Main function to start and run the game.
reset_and_play(): Helper function to reset and start a new game.
