import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
DANCER_COLOR = (255, 255, 255)
NUM_DANCERS = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dance Inspired by 'Tiny Dancer'")

# Define a Dancer class
class Dancer:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.path = []

    def add_point_to_path(self, x, y):
        self.path.append((x, y))

    def move(self):
        if not self.path:
            return
        target_x, target_y = self.path[0]
        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > 0:
            dx /= distance
            dy /= distance
        dx *= self.speed
        dy *= self.speed
        self.x += dx
        self.y += dy
        if abs(target_x - self.x) < self.speed and abs(target_y - self.y) < self.speed:
            self.path.pop(0)

    def draw(self):
        pygame.draw.circle(screen, DANCER_COLOR, (int(self.x), int(self.y)), 20)

# Create a list of dancers
dancers = [Dancer(WIDTH // 2, HEIGHT // 2, 3) for _ in range(NUM_DANCERS)]

# Define the path points for the dancers
path_points = [
    (100, 300),
    (300, 100),
    (500, 400),
    (700, 200),
]

# Add the path points to the dancers' paths
for dancer in dancers:
    for point in path_points:
        dancer.add_point_to_path(*point)

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
