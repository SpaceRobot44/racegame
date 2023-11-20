import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

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
