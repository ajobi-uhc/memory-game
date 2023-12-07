import turtle
import random

NUM_CARDS = 16
NUM_COLS = 4
CARD_SIZE = 100
SCREEN_SIZE = NUM_COLS * CARD_SIZE
GRID_WIDTH = NUM_COLS * CARD_SIZE
GRID_HEIGHT = (NUM_CARDS // NUM_COLS) * CARD_SIZE
cards = []
selected_cards = []
canSelect = True
matched_cards = set()
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)

def init_game():
    global cards
    num_pairs = NUM_CARDS // 2
    card_values = list(range(1, num_pairs + 1)) * 2  # Create pairs
    random.shuffle(card_values)  # Shuffle the card values to randomize them
    cards = [{'value': val, 'matched': False, 'position': i} for i, val in enumerate(card_values)]
    print(cards)

def shuffle_cards():
    global cards
    random.shuffle(cards)

# Function to handle card selection
def select_card(x, y):
    global selected_cards
    global canSelect
    if canSelect == False: 
        print("I AM SELECTED", canSelect)
        return
    print("select")
    print(x, y)
    card_index = get_card_index(x, y)
    if card_index is not None and card_index not in selected_cards and card_index not in matched_cards:
        selected_cards.append(card_index)
        draw_card(cards[card_index]['position'], cards[card_index]['value'], False)
        if len(selected_cards) == 2:
            wn.ontimer(check_match, 1000)
            canSelect = False
        elif len(selected_cards) > 2:
            selected_cards.pop(0)
            draw_grid()


def draw_grid():
    turtle.speed('fastest')  # Speed up the drawing
    turtle.penup()

    # Calculate the total grid width and heigh

    # Starting position (top-left corner of the grid)
    start_x = -GRID_WIDTH // 2
    start_y = GRID_HEIGHT // 2

    # Draw the grid of cards
    for row in range(NUM_CARDS // NUM_COLS):
        for col in range(NUM_COLS):
            x = start_x + col * CARD_SIZE
            y = start_y - row * CARD_SIZE

            # Draw a single card square
            turtle.goto(x, y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(CARD_SIZE)
                turtle.right(90)
            turtle.penup()
    turtle.hideturtle()  # Hide the turtle cursor after drawing

# Function to draw a single card
# Function to draw a single card
def draw_card(position, value, face_down=True):
    print("drawing card at position", position)
    x, y = get_card_coordinates(position)
    print("drawing card", position, "at", x, y)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor('white' if face_down else 'lightblue')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(CARD_SIZE)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

    if not face_down:
        # Move to the center of the card to write the number
        turtle.goto(x + CARD_SIZE / 2, y + CARD_SIZE / 2 - 15)  # Adjust as needed
        turtle.write(value, align="center", font=("Arial", 18, "normal"))


# Function to reset the game
def reset_game():
    global cards, selected_cards, matched_cards
    selected_cards = []
    matched_cards = set()
    shuffle_cards()
    draw_grid()

# Helper functions
def get_card_index(x, y):
    half_width = SCREEN_SIZE // 2
    half_height = SCREEN_SIZE // 2

    # Adjust the click coordinates to be relative to the bottom-left corner of the grid
    grid_x = x + half_width
    grid_y = half_height - y

    # Make sure the click is within the bounds of the grid
    if not (0 <= grid_x < SCREEN_SIZE and 0 <= grid_y < SCREEN_SIZE):
        return None

    col = int(grid_x // CARD_SIZE)
    row = int(grid_y // CARD_SIZE)

    # Calculate the card index based on the row and column
    card_index = row * NUM_COLS + col

    # Debug prints
    print(f"Click coordinates: ({x}, {y})")
    print(f"Adjusted grid coordinates: ({grid_x}, {grid_y})")
    print(f"Grid position: (Row {row}, Col {col})")
    print(f"Card index: {card_index}")

    return card_index


def get_card_coordinates(position):
    col = position % NUM_COLS
    row = position // NUM_COLS

    # Calculate the correct starting y-coordinate
    start_x = -GRID_WIDTH // 2
    start_y = (GRID_HEIGHT // 2) - CARD_SIZE  # Adjust start_y by subtracting CARD_SIZE

    # Calculate the x and y coordinates based on the card's column and row
    x = start_x + col * CARD_SIZE
    y = start_y - row * CARD_SIZE  # No need to subtract CARD_SIZE again, as it's included in start_y

    return x, y



# Function to check for matches
def check_match():
    global selected_cards, matched_cards
    global canSelect
    if len(selected_cards) == 2:
        card1, card2 = selected_cards[0], selected_cards[1]
        if cards[card1]['value'] == cards[card2]['value']:
            # It's a match
            matched_cards.update([card1, card2])
        else:
            # Not a match, turn both cards back over
            draw_card(card1, cards[card1]['value'], True)
            draw_card(card2, cards[card2]['value'], True)

        selected_cards = []

        # Check if the game is over
        if len(matched_cards) == NUM_CARDS:
            game_over()
    canSelect = True    

def game_over():
    # Display a game over message on the screen
    turtle.penup()
    turtle.goto(0, 0)  # Position the turtle at the center of the screen
    turtle.color('black')  # Set the text color
    turtle.write("Game Over! You found all the matches.", align="center", font=("Arial", 19, "normal"))
    turtle.hideturtle()  # Hide the turtle cursor after writing


def play_game():
    # Set up the game window
    wn.clear()
    turtle.clear()
    wn.bgcolor("white")
    turtle.speed('fastest')
    turtle.hideturtle()

    # Initialize and shuffle the cards
    init_game()

    # Draw the initial grid of face-down cards
    draw_grid()

    # Set up the mouse click event handler
    wn.onscreenclick(select_card)

    # Start the Turtle graphics event loop
    wn.mainloop()

# Helper function to reset and play the game
def reset_and_play():
    reset_game()
    play_game()

play_game()