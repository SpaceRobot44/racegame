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

        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 255, 0))

        self.rect = self.image.get_rect()
        self.speed = random.randint(1, 8)

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.set_initial_position()

    def set_initial_position(self):
        middle_width = self.screen_width / 2
        lower_x = middle_width - 150
        upper_x = middle_width + 150
        self.rect.x = random.randint(lower_x, upper_x)
        self.rect.y = 0

    def update(self):
        self.rect.y += self.speed
    # THE COINS WILL MAINTAIN A FAST LOOPING SPEED AFTER REACHING THE MINIMUM SPEED, CAUSING A RANDOM LOOP
        if self.rect.y > self.screen_height:
            self.reset()
            self.speed -= 0 # THE SPEED AT WHICH THE COINS COME ON THE SCREEN AFTER REACHING THE BOTTOM
            if self.speed < 8: # MINIMUM VALUE FOR THE SPEED
                self.speed = random.randint(8, 12) # RANDOM RANGE OF VALUES THAT THE COINS CAN LOOP FROM

    def reset(self):
        self.set_initial_position()
        self.speed = random.randint(8, 12)
        self.scatter_x_position()

    def scatter_x_position(self):
        x_pos = random.randint(self.screen_width / 2, self.screen_width / 2)
        x_offset = random.randint(-150, 150)
        self.rect.x = x_pos + x_offset


def create_coinfall(screen_width, screen_height, num_coins):
    for _ in range(num_coins):
        coin = Coin(screen_width, screen_height) # COMBINES THE DIMENSIONS FROM THE ABOVE COIN CLASS
        coinfall.add(coin)

    return coinfall

coinfall = pygame.sprite.Group() # ESTABLISH COINFALL AS A GROUP

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

    class Coin(pygame.sprite.Sprite):
        def __init__(self, screen_width, screen_height):
            super().__init__()

            self.image = pygame.Surface((15, 15))
            self.image.fill((255, 255, 0))

            self.rect = self.image.get_rect()
            self.speed = random.randint(1, 8)

            self.screen_width = screen_width
            self.screen_height = screen_height

            self.set_initial_position()

        def set_initial_position(self): # INITIAL POSITION OF THE COINS BOUNDS
            middle_width = self.screen_width / 2
            lower_x = middle_width - 175
            upper_x = middle_width + 175
            self.rect.x = random.randint(lower_x, upper_x)
            self.rect.y = 0

        # THE COINS WILL RESET TO THEIR INITIAL POSITION ONCE THEY REACH THE BOTTOM
        def update(self):
            self.rect.y += self.speed
            if self.rect.y > self.screen_height:
                self.reset()
                self.speed -= 1
                if self.speed < 8:
                    self.speed = random.randint(8, 12) # RANDOM RANGE SPEED AT WHICH THE COINS COME ON THE SCREEN

        def reset(self):
            self.set_initial_position()
            self.speed = random.randint(8, 12)
            self.scatter_x_position()

        def scatter_x_position(self):
            x_pos = random.randint(self.screen_width / 2, self.screen_width / 2) # RANDOM X VALUES THE COINS GO TO
            # WITHIN THE PAREMETERS OF THE SCREEN I SET
            x_offset = random.randint(-150, 150)
            self.rect.x = x_pos + x_offset

    def create_coinfall(screen_width, screen_height, num_coins):
        coinfall = pygame.sprite.Group()  # Create a sprite group to hold the coins
        for _ in range(num_coins):
            coin = Coin(screen_width, screen_height)
            coinfall.add(coin)

        return coinfall

    # Create the coinfall group
    coinfall = create_coinfall(SCREEN_WIDTH, SCREEN_HEIGHT, num_coins=60) # NUMBER OF COINS ON THE SCREEN AT A TIME

    return screen, SCREEN_WIDTH, SCREEN_HEIGHT, grass_rotated, road_rotated, snowfall, coinfall, road_x_min, road_x_max