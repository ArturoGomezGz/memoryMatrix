import pygame
import random

pygame.init()

# Constants
GRID_SIZE = 5
CELL_SIZE = 80
SCREEN_SIZE = (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize display
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Simon Game")

# Game variables
sequence = []
user_sequence = []
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // CELL_SIZE
            col = x // CELL_SIZE
            color = row * GRID_SIZE + col  # Unique number for each color

            user_sequence.append(color)

            # Check if the user's sequence is correct
            if len(user_sequence) == len(sequence):
                if user_sequence == sequence:
                    sequence.append(random.randint(0, GRID_SIZE * GRID_SIZE - 1))
                    user_sequence = []
                else:
                    print("Wrong sequence! Game Over.")
                    running = False

    # Draw grid and colors
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = row * GRID_SIZE + col
            pygame.draw.rect(screen, (color * 50, 255 - color * 50, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    # Show the sequence to the player
    pygame.time.delay(1000)  # Delay between each color
    for color in sequence:
        row = color // GRID_SIZE
        col = color % GRID_SIZE
        pygame.draw.rect(screen, (color * 50, 255 - color * 50, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        pygame.time.delay(1000)  # Delay before the next color
        pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()

    # Add a new random color to the sequence
    if len(user_sequence) == len(sequence):
        sequence.append(random.randint(0, GRID_SIZE * GRID_SIZE - 1))
        user_sequence = []

pygame.quit()