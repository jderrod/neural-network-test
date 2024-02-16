# game_objects.py
import pygame
import random
from settings import *

# Modify the Dot class in game_objects.py

class Dot:
    def __init__(self, x, y, screen_width, screen_height):
        self.x = x
        self.y = y
        self.size = dot_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)


class Food:
    def __init__(self):
        self.x = random.randint(0, window_width - food_size)
        self.y = random.randint(0, window_height - food_size)
        self.size = food_size

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.size)

    #def respawn(self):
    #    """Reposition the food to a new random location."""
    #    self.x = random.randint(0, window_width - food_size)
    #    self.y = random.randint(0, window_height - food_size)

