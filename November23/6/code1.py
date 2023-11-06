import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Healing Heart Visual Experiment")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Heart coordinates
heart_x = WIDTH // 2
heart_y = HEIGHT // 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw a heart shape (you can modify this to create your own design)
    pygame.draw.polygon(screen, RED, [(heart_x, heart_y - 50), (heart_x - 50, heart_y), (heart_x + 50, heart_y)])
    pygame.draw.circle(screen, RED, (heart_x - 25, heart_y - 25), 25)
    pygame.draw.circle(screen, RED, (heart_x + 25, heart_y - 25), 25)

    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()
