import pygame
import sys

def sub_menu(screen,font, help_menu):
    # Load and scale the background image
    menu_image = pygame.image.load("assets/christmas/PNG/Menu Pic.png")
    menu_image = pygame.transform.scale(menu_image, (screen.get_width(), screen.get_height()))

    # Define button properties
    button_width = 300
    button_height = 100
    button_color = (0, 0, 0)  # Button color

    # Puts all coordinates in middle and then adjust height
    # Start Game Button
    start_button_x = (screen.get_width() - button_width) // 2
    start_button_y = 250
    start_button_rect = pygame.Rect(start_button_x, start_button_y, button_width, button_height)

    # Help Button
    help_button_x = (screen.get_width() - button_width) // 2
    help_button_y = 350
    help_button_rect = pygame.Rect(help_button_x, help_button_y, button_width, button_height)

    # Exit Button
    exit_button_x = (screen.get_width() - button_width) // 2
    exit_button_y = 450
    exit_button_rect = pygame.Rect(exit_button_x, exit_button_y, button_width, button_height)

    # Main loop for the sub-menu
    while True:
        screen.blit(menu_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return  # Return to start the game
                elif help_button_rect.collidepoint(event.pos):
                    from help_menu import help_menu  # Import here to avoid circular import
                    help_menu(screen, font)  # Open Help Menu
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Draw buttons
        pygame.draw.rect(screen, button_color, start_button_rect)
        pygame.draw.rect(screen, button_color, help_button_rect)
        pygame.draw.rect(screen, button_color, exit_button_rect)

        # Add text to the buttons
        start_text = font.render('Start Game', True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=start_button_rect.center)
        help_text = font.render('Help', True, (255, 255, 255))
        help_text_rect = help_text.get_rect(center=help_button_rect.center)
        exit_text = font.render('Exit', True, (255, 255, 255))
        exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)

        screen.blit(start_text, start_text_rect)
        screen.blit(help_text, help_text_rect)
        screen.blit(exit_text, exit_text_rect)

        pygame.display.update()
