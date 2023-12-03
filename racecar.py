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

    def update(self, road_speed, road_x_min, road_x_max):
        self.rect.y += self.velocity + road_speed  # Adjust the car position based on road scrolling speed

        # Limit the velocity to the defined range
        self.velocity = max(self.min_velocity, min(self.velocity, self.max_velocity))

        # Ensure the car stays within the road boundaries
        if self.rect.x < road_x_min:
            self.rect.x = road_x_min
        elif self.rect.right > road_x_max:
            self.rect.right = road_x_max

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        self.rect.x -= 25  # Adjust the leftward movement speed

    def move_right(self):
        self.rect.x += 25  # Adjust the rightward movement speed

    def accelerate_forward(self):
        # Adjust the acceleration value as needed
        self.velocity += -5

    def decelerate(self):
        # Adjust the deceleration value as needed
        self.velocity -= -1
    def accelerate(self):
        # Adjust the double acceleration
        self.velocity += -30
