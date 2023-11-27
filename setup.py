# setup.py

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

    return screen, SCREEN_WIDTH, SCREEN_HEIGHT, grass_rotated, road_rotated
def draw_trees(screen, road_x, road_width, tree_spacing=100):
    """Draw trees along the side of the road."""
    tree_image = pygame.image.load('assets/christmas/PNG/tree_top.png')

    # Set initial tree position
    tree_x = road_x - tree_image.get_width()  # Adjust as needed

    while tree_x < road_x + road_width:
        # Draw the tree
        screen.blit(tree_image, (tree_x, 0))  # Adjust the vertical position as needed

        # Move to the next tree position
        tree_x += tree_spacing
