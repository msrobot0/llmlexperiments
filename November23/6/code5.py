import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yvonne Rainer's Choreography Illustration")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dancer coordinates
dancer_x = WIDTH // 2
dancer_y = HEIGHT // 2

# Dancer movement variables
move_x = 0
move_y = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_x = -1
    if keys[pygame.K_RIGHT]:
        move_x = 1
    if keys[pygame.K_UP]:
        move_y = -1
    if keys[pygame.K_DOWN]:
        move_y = 1

    screen.fill(WHITE)

    # Draw the dancer (a simple rectangle for illustration)
    pygame.draw.rect(screen, BLACK, (dancer_x, dancer_y, 50, 50))

    # Update dancer position
    dancer_x += move_x
    dancer_y += move_y

    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()

