import pygame
import sys
from setup import setup
from racecar import Car

def center_lines(screen, road_x, road_width, line_width, line_gap):
    for y in range(0, screen.get_height(), line_gap):
        pygame.draw.rect(screen, (255, 255, 255), (road_x + road_width // 2 - line_width // 2, y, line_width, line_gap // 1.5))

def main():
    """The main game loop."""

    # Call the setup function to get the screen and other variables
    screen, SCREEN_WIDTH, SCREEN_HEIGHT, GRASS, ROAD = setup()

    # Rotate the images by 90 degrees
    GRASS = pygame.transform.rotate(GRASS, -90)
    ROAD = pygame.transform.rotate(ROAD, -90)

    # Set the initial road width
    road_width = 500  # Adjust the initial width as needed

    # Create an instance that allows the car to pass into the screen
    car = Car(screen, road_width)

    # Dotted line parameters
    line_width = 10
    line_gap = 30

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with rotated grass
        for y in range(0, SCREEN_HEIGHT, GRASS.get_height()):
            for x in range(0, SCREEN_WIDTH, GRASS.get_width()):
                screen.blit(GRASS, (x, y))

        # Calculate the x-coordinate for the road to keep it centered
        road_x = SCREEN_WIDTH // 2 - road_width // 2

        # Draw a rotated road in the middle of the screen
        for y in range(0, SCREEN_HEIGHT, ROAD.get_height()):
            screen.blit(pygame.transform.scale(ROAD, (road_width, ROAD.get_height())), (road_x, y))

        # Draw dotted white lines down the center of the road
        center_lines(screen, road_x, road_width, line_width, line_gap)

        # Update the car
        car.update()

        # Draw the car on the screen
        car.draw(screen)

        # Update the display
        pygame.display.flip()

        # Add a short delay to control the frame rate
        pygame.time.delay(120)

if __name__ == "__main__":
    main()
