import pygame

def effects(screen, score, speed, font):
    # Define colors
    text_color = (255, 255, 255)  # White color

    # Render the score text
    score_text = font.render(f"Score: {score}", True, text_color)
    score_rect = score_text.get_rect()
    score_rect.topleft = (10, 10)  # Adjust the position as needed

    # Render the speed text
    speed_text = font.render(f"Speed: {speed} MPH", True, text_color)
    speed_rect = speed_text.get_rect()
    speed_rect.topleft = (10, 40)  # Adjust the position as needed

    # Draw the score and speed on the screen
    screen.blit(score_text, score_rect)

