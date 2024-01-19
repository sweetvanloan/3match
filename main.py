import random

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E']

def initialize_board(width, height):
    """ Initialize the game board with random elements. """
    return [[random.choice(ELEMENTS) for _ in range(width)] for _ in range(height)]

def print_board(board):
    """ Print the game board. """
    for row in board:
        print(' '.join(row))
    print()

# Different board sizes
board_sizes = {
    "Standard": (8, 8),
    "Special": (8, 10),
    "Intermediate": (10, 10),
    "Hard": (10, 15),
    "Super Hard": (15, 20),
    "Advanced": (20, 25),
    "Challenge 1": (20, 0)  # Note: A board with 0 height will be empty
}

# Example of creating and displaying a board
size_label = "Standard"  # Choose from the keys of board_sizes
width, height = board_sizes[size_label]
game_board = initialize_board(width, height)
print(f"{size_label} Board:")
print_board(game_board)
