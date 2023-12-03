
import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN
import racecar
import sys

def controls(car):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        car.move_left()

    if keys[pygame.K_RIGHT]:
        car.move_right()

    if keys[pygame.K_UP]:
        car.accelerate()

    if keys[pygame.K_DOWN]:
        car.decelerate()


def mouse_click():
    print("Checking for mouse clicks...")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse click detected!")
            mouse_x, mouse_y = event.pos

            # Define the coordinates for the start button
            start_button_rect = pygame.Rect(100, 200, 100, 50)

            # Check if the mouse click is within the start button
            if start_button_rect.collidepoint(mouse_x, mouse_y):
                print("Mouse click within the start button!")
                return True  # User clicked the start button

    return False  # No relevant click detected
