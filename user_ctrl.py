import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE
import sys

def controls(car):
    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        car.move_left()

    if keys[K_RIGHT]:
        car.move_right()

    if keys[K_UP]:
        car.accelerate_forward()

    if keys[K_DOWN]:
        car.decelerate()

    if keys[K_SPACE]:
        car.accelerate

def mouse_click():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Define the coordinates for the start button
            start_button_rect = pygame.Rect(100, 200, 100, 50)

            # Check if the mouse click is within the start button
            if start_button_rect.collidepoint(mouse_x, mouse_y):
                return True  # User clicked the start button

    return False  # No relevant click detected