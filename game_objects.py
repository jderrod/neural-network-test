# game_objects.py
import pygame
import random
from settings import window_width, window_height, dot_size, food_size, WHITE, RED

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = dot_size
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

    def respawn(self):
        self.x = random.randint(0, window_width - food_size)
        self.y = random.randint(0, window_height - food_size)
