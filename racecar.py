import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

class Car(pygame.sprite.Sprite):
    def __init__(self, screen, road_width):
        super().__init__()

        # Load the car image
        self.image = pygame.image.load('assets/PNG/Cars/car_blue_small_4.png')
        # Adjust the scale factor to make the car bigger
        self.image = pygame.transform.scale(self.image,
                                            (int(self.image.get_width() * 1), int(self.image.get_height() * 1)))
        self.rect = self.image.get_rect()

        # Set the initial position of the car at the bottom center of the screen
        self.rect.x = screen.get_width() // 2 - self.rect.width // 2
        self.rect.y = screen.get_height() // 1.25 - self.rect.height // 1  # Bottom of the screen

        self.velocity = 0  # Change the velocity of the car
        self.max_velocity = 200  # Maximum velocity
        self.min_velocity = 0  # Minimum velocity

        self.acceleration = 5  # Adjust the acceleration value as needed
        self.deceleration = 1  # Adjust the deceleration value as needed

    def update(self, road_speed, road_x_min, road_x_max):
        keys = pygame.key.get_pressed()

        # Check if any arrow keys are pressed
        if any(keys):
            # Adjust the car position based on road scrolling speed and positive velocity
            self.rect.y += max(0, self.velocity + road_speed)

            # Limit the velocity to the defined range
            self.velocity = max(self.min_velocity, min(self.velocity, self.max_velocity))

            # Ensure the car stays within the road boundaries
            if self.rect.x < road_x_min:
                self.rect.x = road_x_min
                self.velocity = 0  # Stop the car if it hits the left boundary
            elif self.rect.right > road_x_max:
                self.rect.right = road_x_max
                self.velocity = 0  # Stop the car if it hits the right boundary
            else:
                self.velocity = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        self.rect.x -= 8  # Adjust the leftward movement speed

    def move_right(self):
        self.rect.x += 8  # Adjust the rightward movement speed

    def accelerate(self):
        # Move the car forward
        self.rect.y -= 4

    def decelerate(self):
        # Move the car backward
        self.rect.y += 4

