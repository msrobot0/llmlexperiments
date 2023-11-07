import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Expanding Random Numbers")

# Define font and initial text
font = pygame.font.Font(None, 36)
number = random.randint(1, 100)
text = font.render(str(number), True, (255, 255, 255))

# Define initial text position and scale
text_x, text_y = screen_width // 2, screen_height // 2
scale = 1.0

# Animation properties
expansion_rate = 0.01

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Expand the text
    scale += expansion_rate

    # Generate a new random number when the text is large enough
    if scale > 2.0:
        number = random.randint(1, 100)
        text = font.render(str(number), True, (255, 255, 255))
        scale = 1.0

    # Scale and draw the text
    text_scaled = pygame.transform.scale(text, (int(text.get_width() * scale), int(text.get_height() * scale)))
    text_rect = text_scaled.get_rect(center=(text_x, text_y))
    screen.blit(text_scaled, text_rect)

    pygame.display.flip()

    # Control the frame rate (adjust as needed)
    pygame.time.delay(50)

pygame.quit()

