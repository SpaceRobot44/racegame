import pygame
import math
import sys
from setup import setup
from racecar import Car

def center_lines(screen, road_x, road_width, line_width, line_gap, line_y):
    for y in range(line_y, screen.get_height(), line_gap):
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

    # Initial starting positions for grass, road, and lines scrolling
    grass_y = 0
    road_y = -10000
    line_y = -10000

    num_l = int(10) # Allows me to place any number want into my loop function below because it's established
    num_r = int(10)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the grass position to create an infinite scrolling effect
        grass_y += 7  # Adjust the scrolling speed as needed

        # Fill the screen with rotated grass
        for y in range(grass_y, SCREEN_HEIGHT, GRASS.get_height()):
            for x in range(0, SCREEN_WIDTH, GRASS.get_width()):
                screen.blit(GRASS, (x, y))

        # If the grass scrolls off the screen, reset its position, so it loops
        if grass_y > GRASS.get_height():
            grass_y = 0

        # Update the road position to create an infinite scrolling effect
        road_y += -25  # Adjust the scrolling speed as needed

        # Calculate the x-coordinate for the road to keep it centered
        road_x = SCREEN_WIDTH // 2 - road_width // 2

        # Draw a rotated road in the middle of the screen
        for y in range(road_y, SCREEN_HEIGHT, ROAD.get_height()):
            screen.blit(pygame.transform.scale(ROAD, (road_width, ROAD.get_height())), (road_x, y))

        # If the road scrolls off the screen, reset its position, so it loops
        if road_y > ROAD.get_height():
            road_y -= num_r*ROAD.get_height() # By making the number less than the set number, it causes it to loop

        # Update the white lines position to create an infinite scrolling effect
        line_y += -50  # Adjust the scrolling speed as needed

        # Draw dotted white lines down the center of the road
        center_lines(screen, road_x, road_width, line_width, line_gap, line_y)

        # If the lines go off the screen, reset their position to create a loop
        if line_y > line_gap:
            line_y -= num_l*line_gap # Multiplying the line gap by a large number increases the time until the loop resets

        # Update the car
        car.update(5) # Allows me to pass in the scrolling speed as an argument

        # Draw the car on the screen
        car.draw(screen)

        # Update the display
        pygame.display.flip()

        # Add a short delay to control the frame rate
        pygame.time.delay(120)

if __name__ == "__main__":
    main()
