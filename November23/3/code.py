import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
DANCER_COLOR = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dancer Follows Line")

# Define a Dancer class
class Dancer:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.path = []  # List to store the path points
        self.current_path_index = 0

    def add_point_to_path(self, x, y):
        self.path.append((x, y))

    def move(self):
        if self.current_path_index < len(self.path):
            target_x, target_y = self.path[self.current_path_index]
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
                self.current_path_index += 1

    def draw(self):
        pygame.draw.circle(screen, DANCER_COLOR, (int(self.x), int(self.y)), 20)

# Create a dancer
dancer = Dancer(WIDTH // 2, HEIGHT // 2, 3)

# Define the path points
path_points = [
    (100, 100),
    (700, 100),
    (700, 500),
    (100, 500),
]

# Add the path points to the dancer's path
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

    dancer.move()
    dancer.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
