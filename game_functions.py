# game_functions.py
import sys
import pygame
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
    if dot.moving_up and dot.y - dot.size > 0:
        dot.y -= dot_speed
    if dot.moving_down and dot.y + dot.size < dot.screen_height:
        dot.y += dot_speed
    if dot.moving_left and dot.x - dot.size > 0:
        dot.x -= dot_speed
    if dot.moving_right and dot.x + dot.size < dot.screen_width:
        dot.x += dot_speed

def check_collision(dot, food):
    """Check if the dot collides with the food."""
    distance = ((dot.x - food.x) ** 2 + (dot.y - food.y) ** 2) ** 0.5
    if distance < dot.size + food.size:
        return True
    return False

def update_dot_direction_nn(dot, action):
    """
    Update the dot's movement direction based on the neural network's output.
    
    :param dot: The dot object to update.
    :param action: The action determined by the neural network (0: up, 1: down, 2: left, 3: right).
    """
    # Reset any previous movement
    dot.moving_up = dot.moving_down = dot.moving_left = dot.moving_right = False

    if action == 0:  # Up
        dot.moving_up = True
    elif action == 1:  # Down
        dot.moving_down = True
    elif action == 2:  # Left
        dot.moving_left = True
    elif action == 3:  # Right
        dot.moving_right = True

    update_dot_position(dot)
    # Since dot is updated in place, we technically don't need to return it,
    # but doing so can make the function's effect more explicit.
    return dot


