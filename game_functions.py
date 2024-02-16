# game_functions.py
import pygame
import sys
from settings import dot_speed

def check_events(dot):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            update_dot_direction(dot, event.key, True)
        elif event.type == pygame.KEYUP:
            update_dot_direction(dot, event.key, False)

def update_dot_direction(dot, key, is_key_down):
    """Update the dot's movement direction based on key presses."""
    if key == pygame.K_UP:
        dot.moving_up = is_key_down
    elif key == pygame.K_DOWN:
        dot.moving_down = is_key_down
    elif key == pygame.K_LEFT:
        dot.moving_left = is_key_down
    elif key == pygame.K_RIGHT:
        dot.moving_right = is_key_down

def update_dot_position(dot):
    """Update the dot's position based on movement flags."""
    if dot.moving_up:
        dot.y -= dot_speed
    if dot.moving_down:
        dot.y += dot_speed
    if dot.moving_left:
        dot.x -= dot_speed
    if dot.moving_right:
        dot.x += dot_speed

def check_collision(dot, food):
    """Check if the dot collides with the food."""
    distance = ((dot.x - food.x) ** 2 + (dot.y - food.y) ** 2) ** 0.5
    if distance < dot.size + food.size:
        return True
    return False
