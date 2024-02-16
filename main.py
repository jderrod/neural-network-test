import pygame
import sys
import torch
from settings import *
from game_objects import Dot, Food
import game_functions as gf
from neural_network import get_model

# Initialize Pygame
pygame.init()

# Create the display window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Dot NN Game")

# Neural Network Model
model = get_model()

# Game loop flag
running = True

# Game objects
dot = Dot(window_width // 2, window_height // 2, window_width, window_height)
food = Food()

while running:
    # Event checking (e.g., for quitting the game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Prepare the state for the neural network
    state = torch.tensor([food.x - dot.x, food.y - dot.y], dtype=torch.float32)

    # Use the neural network to choose an action
    with torch.no_grad():
        action_probabilities = model(state.unsqueeze(0))
        action = torch.argmax(action_probabilities).item()
        print("Chosen action:", action)  # Check the chosen action


    # Use the neural network to choose an action and update the dot's direction
    dot = gf.update_dot_direction_nn(dot, action)  # No need to unpack with "_"


    # Render the game
    screen.fill(BLACK)
    dot.draw(screen)
    food.draw(screen)
    pygame.display.flip()

    # Add a small delay to make the game visually followable
    pygame.time.delay(100)

# Quit Pygame
pygame.quit()
sys.exit()
