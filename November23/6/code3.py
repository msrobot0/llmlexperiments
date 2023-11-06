import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ayurvedic Heart Healing")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ayurvedic elements
ELEMENTS = ["Earth", "Water", "Fire", "Air", "Ether"]

# Heart coordinates
heart_x = WIDTH // 2
heart_y = HEIGHT // 2

# Heart size
heart_scale = 1.0

# Interaction variables
element_index = 0
animate = False

# Create a font
font = pygame.font.Font(None, 36)

def draw_heart(x, y, scale):
    # Draw a heart shape
    pygame.draw.polygon(screen, RED, [(x, y - 50 * scale), (x - 50 * scale, y), (x + 50 * scale, y)])
    pygame.draw.circle(screen, RED, (x - 25 * scale, y - 25 * scale), 25 * scale)
    pygame.draw.circle(screen, RED, (x + 25 * scale, y - 25 * scale), 25 * scale)

def display_element(element):
    element_text = font.render(f"Ayurvedic Element: {element}", True, RED)
    screen.blit(element_text, (10, 10))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                animate = not animate
            elif event.key == pygame.K_RIGHT:
                element_index = (element_index + 1) % len(ELEMENTS)
            elif event.key == pygame.K_LEFT:
                element_index = (element_index - 1) % len(ELEMENTS)

    screen.fill(WHITE)

    if animate:
        # Animate the heart's scale
        heart_scale = 1.0 + 0.5 * math.sin(pygame.time.get_ticks() / 1000)

    draw_heart(heart_x, heart_y, heart_scale)
    display_element(ELEMENTS[element_index])

    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()

