import pygame
import sys
from setup import setup, coinfall
from racecar import Car
from user_ctrl import controls, mouse_click
from main_menu import main_menu
from effects import effects
import random
from sounds import play_music, stop_music
import os


def checkered_border(screen, x, y, width, height, num_squares):
    square_width = width / num_squares
    #  Determines the color of each square based on whether the index i is even or odd.
    for i in range(num_squares):
        color = (255, 0, 0) if i % 2 == 0 else (255, 255, 255)
        pygame.draw.rect(screen, color, (x + i * square_width, y, square_width, height))

def center_lines(screen, road_x, road_width, line_width, line_gap, line_y):
    for y in range(line_y, screen.get_height(), line_gap):
        pygame.draw.rect(screen, (255, 255, 255), (road_x + road_width // 2 - line_width // 2, y, line_width, line_gap // 1.5))

def street_lines(screen, road_x, road_width, line_width, line_gap, line_y):
    for y in range(line_y, screen.get_height(), line_gap):
        pygame.draw.rect(screen, (255, 255, 255),
                         (road_x + road_width // 1.35 - line_width // 2, y, line_width, line_gap // 1.5))
        checkered_border(screen, road_x - line_width // 2, y, line_width * 3, line_gap // 1, num_squares=5)

def street_lines2(screen, road_x, road_width, line_width, line_gap, line_y):
    for y in range(line_y, screen.get_height(), line_gap):
        pygame.draw.rect(screen, (255, 255, 255),
                         # ALLOWS FOR THE CHANGE IN POSITION FOR THE DOTTED LINES OVER THE SCREEN
                         (road_x + road_width // 4 - line_width // 2, y, line_width, line_gap // 1.5))
        checkered_border(screen, road_x + road_width - line_width * 2, y, line_width * 3, line_gap // 1, num_squares=5)


def display_score(screen, font, score):
    # Define the font path and size
    font_path = 'assets/Extras/ka1.ttf'
    font_size = 24

    # Load the font
    font = pygame.font.Font(font_path, font_size)

    # Create a text surface with the score and font
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

    # Set the position of the text
    text_position = (10, 10)

    # Blit the text onto the screen
    screen.blit(score_text, text_position)


def main():
    # Call the setup function to get the screen and other variables
    screen, SCREEN_WIDTH, SCREEN_HEIGHT, GRASS, ROAD, snowfall, coinfall, road_x_min, road_x_max = setup()

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
    grass_y = -50000
    road_y = -50000
    line_y = -50000

    # Allows me to place any number I want into my loop function below because it's established
    num_l = int(15)
    num_r = int(15)
    num_g = int(10)

    # The state which the game is in
    game_state = "main_menu" # Initially set to main menu
    # The function above helps identify whether the game is in the menu or actual game

    # Set the path to your music file
    music_path = os.path.join('assets/christmas/Music/music 1.mp3')
    # Play music with looping
    play_music(music_path, loop=True)

    score = 0


    # Game loop
    while True:
        # Establish the road speed
        road_speed = 2

        # CHECKS FOR EVENTS WITHIN THE GAME
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state == "main_menu": # IF TRUE, THE MAIN MENU IS DISPLAYED
            font = pygame.font.Font(None, 36)  # Adjust font size and type as needed
            main_menu(screen, font)  # Now passing the font argument

            # Check for user input to switch game state
            user_clicked_start_button = mouse_click()

            if user_clicked_start_button is not None:
                game_state = "race_game"

            user_clicked_help_button = False  # Reset help button flag

            # UPDATES THE CONTROLS ON THE SCREEN
            # ALSO LINKED TO OTHER MODULES
        elif game_state == "race_game":
            # Controls for the user car
            controls(car)

            # Update the snowfall effect
            snowfall.update()

            # Update the coinfall effect
            coinfall.update()

            # Update the grass position to create an infinite scrolling effect
            grass_y += 10  # Adjust the scrolling speed as needed

            for y in range(grass_y, SCREEN_HEIGHT, GRASS.get_height()):
                for x in range(0, SCREEN_WIDTH, GRASS.get_width()):
                    screen.blit(GRASS, (x, y))

            # If the grass scrolls off the screen, reset its position, so it loops
            if grass_y > GRASS.get_height():
                grass_y -= num_g * GRASS.get_height()

            # Update the road position to create an infinite scrolling effect
            road_y += 25  # Adjust the scrolling speed as needed

            road_x = SCREEN_WIDTH // 2 - road_width // 2

            # BLITS DIFFERENT Y COORDINATES WHEN SCROLLING TO CREATE THE EFFECT
            for y in range(road_y, SCREEN_HEIGHT, ROAD.get_height()):
                screen.blit(pygame.transform.scale(ROAD, (road_width, ROAD.get_height())), (road_x, y))

            # If the road scrolls off the screen, reset its position, so it loops
            if road_y > ROAD.get_height():
                road_y -= num_r * ROAD.get_height()

            # Update the white lines position to create an infinite scrolling effect
            line_y += 3  # Adjust the scrolling speed as needed

            center_lines(screen, road_x, road_width, line_width, line_gap, line_y)
            street_lines(screen, road_x, road_width, line_width, line_gap, line_y)
            street_lines2(screen, road_x, road_width, line_width, line_gap, line_y)

            car.update(road_speed, road_x_min, road_x_max)
            car.draw(screen)
            snowfall.draw(screen)
            coinfall.draw(screen)

            # Check for collisions between car and coinfall sprites
            result = pygame.sprite.spritecollide(car, coinfall, True)  # COINFALL is where my Coin class is located
            if result:
                score += len(result)  # IF A COLLISION OCCURS, THE COINS ARE REMOVED AND THE SCORE IS UPDATED

            # Draw the score and speed on the screen
            display_score(screen, font, score)

            pygame.display.flip()
            pygame.time.delay(60)

    # Stop the music when the game exits
    stop_music()

if __name__ == "__main__":
    main()
