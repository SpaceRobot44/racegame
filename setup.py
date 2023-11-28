import pygame
import random

class Snowflake(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        # Set the image and rect for the snowflake
        self.image = pygame.Surface((7, 7))
        self.image.fill((255, 255, 255))  # White color for the snowflake
        self.rect = self.image.get_rect()

        # Initialize the position and falling speed
        self.rect.x = random.randint(0, screen_width)
        self.rect.y = random.randint(0, screen_height)
        self.speed = random.randint(1, 8)

        # Store screen dimensions in the object
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        # Move the snowflake down the screen
        self.rect.y += self.speed

        # Reset the position if the snowflake goes off the bottom of the screen
        if self.rect.y > self.screen_height:
            self.rect.y = 0
            self.rect.x = random.randint(0, self.screen_width)

def create_snowfall(screen_width, screen_height, num_snowflakes):
    snowfall = pygame.sprite.Group()

    for _ in range(num_snowflakes):
        snowflake = Snowflake(screen_width, screen_height)
        snowfall.add(snowflake)

    return snowfall






class Coin(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        # Set the image and rect for the coins
        self.image = pygame.Surface((7, 7))
        self.image.fill((255, 255, 0))  # yellow color for the coins
        self.rect = self.image.get_rect()

        # Initialize the position and falling speed
        self.rect.x = random.randint(0, screen_width)
        self.rect.y = random.randint(0, screen_height)
        self.speed = random.randint(1, 8)

        # Store screen dimensions in the object
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update_2(self):
        # Move the snowflake down the screen
        self.rect.y += self.speed

        # Reset the position if the coin goes off the bottom of the screen
        if self.rect.y > self.screen_height:
            self.rect.y = 0
            self.rect.x = random.randint(0, self.screen_width)

def create_coinfall(screen_width, screen_height, num_coins):
    coinfall = pygame.sprite.Group()

    for _ in range(num_coins):
        coin = Coin(screen_width, screen_height)
        coinfall.add(coin)

    return coinfall

def setup():
    """Initialize Pygame and set up the screen."""
    pygame.init()

    # Constants for screen dimensions
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 720

    # Initialize the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Crash Out")

    # Set boundaries for cars on the road
    road_x_min = 320  # Adjust as needed
    road_x_max = SCREEN_WIDTH - 320  # Adjust as needed

    # Load images
    grass_original = pygame.image.load('assets/PNG/Tiles/Grass/land_grass04.png')
    road_original = pygame.image.load('assets/road_textures/roadTexture_38.png')

    # Rotate the images by 90 degrees
    grass_rotated = pygame.transform.rotate(grass_original, -90)
    road_rotated = pygame.transform.rotate(road_original, -90)

    # Create the snowfall group
    snowfall = create_snowfall(SCREEN_WIDTH, SCREEN_HEIGHT, num_snowflakes=125)

    # Create the coinfall group
    coinfall = create_coinfall(SCREEN_WIDTH, SCREEN_HEIGHT, num_coins=125)

    return screen, SCREEN_WIDTH, SCREEN_HEIGHT, grass_rotated, road_rotated, snowfall, coinfall, road_x_min, road_x_max
