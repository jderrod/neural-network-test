# main.py
import pygame
import sys
from settings import *
from game_objects import Dot, Food
import game_functions as gf

def main():
    # Initialize Pygame
    pygame.init()

    # Create the display window
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Dot NN Game")

    # Game objects
    dot = Dot(window_width // 2, window_height // 2)
    food = Food()

    # Game loop flag
    running = True

    # Main game loop
    while running:
        gf.check_events(dot)
        gf.update_dot_position(dot)

        if gf.check_collision(dot, food):
            food.respawn()  # Reposition the food if a collision is detected

        screen.fill(BLACK)
        dot.draw(screen)
        food.draw(screen)

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

main()
