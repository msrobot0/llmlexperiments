import pygame
import sys
import random
import math

# Initialize Pygame


pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alchemical Wedding Animation")
font = pygame.font.Font(None, 36)
# Colors
background_color = (0, 0, 0)
symbol_color = (255, 255, 255)

# Main animation loop
running = True
clock = pygame.time.Clock()

# Symbols representing the union of opposites
symbols = []
# Main animation loop
running = True
clock = pygame.time.Clock()
wedding_happened = False

def generate_symbol():
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    size = random.randint(20, 50)
    rotation = random.uniform(0, 360)
    symbols.append((x, y, size, rotation))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(background_color)

    # Generate new symbols
    if len(symbols) < random.randint(10,50):  # Limit the number of symbols
        generate_symbol()

    # Draw and update symbols
    for symbol in symbols:
        x, y, size, rotation = symbol
        pygame.draw.line(screen, symbol_color, (x, y), (x + size, y), size // 10)
        pygame.draw.line(screen, symbol_color, (x, y), (x, y + size), size // 10)
        pygame.draw.line(screen, symbol_color, (x, y), (x + size, y + size), size // 10)
        pygame.draw.line(screen, symbol_color, (x + size, y), (x + size, y + size), size // 10)
        pygame.draw.line(screen, symbol_color, (x, y + size), (x + size, y + size), size // 10)

        # Rotate the symbols
        rotated_symbol = pygame.transform.rotate(screen, rotation)
        screen.blit(rotated_symbol, (x, y))

    # Check if the "wedding" has happened
    if not wedding_happened and len(symbols) >= 10:
        wedding_happened = True
        wedding_text = font.render("Alchemical Wedding", True, (255, 255, 255))
        screen.blit(wedding_text, (screen_width // 2 - 100, screen_height // 2))
    if wedding_happened:
        wedding_text = font.render("Alchemical Wedding", True, (255, 255, 255))
        screen.blit(wedding_text, (screen_width // 2 - 100, screen_height // 2))

    clock.tick(10)  # Set the frame rate to 30 frames per second
    # Update the display
    pygame.display.flip()

    # Control animation speed
    

# Quit Pygame
pygame.quit()
sys.exit()
