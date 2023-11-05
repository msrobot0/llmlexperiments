import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
DANCER_COLOR = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dance in Code")

# Define a Dancer class
class Dancer:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.x += random.randint(-self.speed, self.speed)
        self.y += random.randint(-self.speed, self.speed)

    def draw(self):
        pygame.draw.circle(screen, DANCER_COLOR, (self.x, self.y), 20)

# Create a list of dancers
dancers = [Dancer(random.randint(0, WIDTH), random.randint(0, HEIGHT), 2) for _ in range(5)]

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for dancer in dancers:
        dancer.move()
        dancer.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

