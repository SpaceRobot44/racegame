import pygame

def setup():
    """Initialize Pygame and set up the screen."""
    pygame.init()

    # Constants for screen dimensions
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 720

    # Initialize the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Crash Out")

    # Load images
    grass_original = pygame.image.load('assets/PNG/Tiles/Grass/land_grass04.png')
    road_original = pygame.image.load('assets/road_textures/roadTexture_38.png')

    # Rotate the images by 90 degrees
    grass_rotated = pygame.transform.rotate(grass_original, -90)
    road_rotated = pygame.transform.rotate(road_original, -90)

    # Resize the rotated road image to cover the entire screen height
    road_rotated = pygame.transform.scale(road_rotated, (SCREEN_HEIGHT, SCREEN_WIDTH))

    return screen, SCREEN_WIDTH, SCREEN_HEIGHT, grass_rotated, road_rotated
