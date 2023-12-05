import pygame
import sys

def main_menu(screen, font):
    # LOAD UP THE SCALE AND BACKGROUND IMAGE
    menu_image = pygame.image.load("assets/christmas/PNG/Menu Pic.png")
    menu_image = pygame.transform.scale(menu_image, (screen.get_width(), screen.get_height()))

    # Christmas colors for the button and title
    button_color = (200, 0, 0)  # Red color
    text_color = (0, 128, 0)  # Green color
    title_color = (255, 0, 0)  # Christmas red for the title

    # Create a bright red box for the button
    button_width = 450
    button_height = 75

    # THIS IS ALSO WHY I USE A DIFFERENT CODE FOR THE START BUTTON
    # Center the button horizontally
    button_x = (screen.get_width() - button_width) // 2

    # Center the button vertically
    button_y = (screen.get_height() - button_height) // 2

    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    # Define the title text and style
    title_text = "JINGLE BELL RACEWAY"
    title_font_size = 60  # Adjust the font size
    title_font = pygame.font.Font('assets/Extras/ka1.ttf', title_font_size)
    title_render = title_font.render(title_text, True, title_color)
    title_rect = title_render.get_rect()

    # Center the title at the top of the screen
    title_rect.centerx = screen.get_width() // 2
    title_rect.y = 50  # Adjust the vertical position as needed

    font_size = 30  # ESTABLISH THE FONT SIZE
    # Load the font file
    font_path = 'assets/Extras/ka1.ttf'
    font = pygame.font.Font(font_path, font_size)

    start_button_text = font.render("Click Here To Start", True, text_color)

    start_button_rect = start_button_text.get_rect()

    # Center the text within the button
    start_button_rect.center = button_rect.center

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the button
                if button_rect.collidepoint(event.pos): # IF CLICKED WITHIN AREA, THE GAME WILL START
                    return  # Return to start the game

        # Draw the background image
        screen.blit(menu_image, (0, 0))

        # Draw the title at the top of the screen
        screen.blit(title_render, title_rect)

        # Draw the button in Christmas red
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(start_button_text, start_button_rect)

        pygame.display.flip()
