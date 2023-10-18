import pygame
import random
import sys
from pydub import AudioSegment
from pydub.generators import Sine

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (135, 206, 235)  # Light Blue
CUP_COLOR = (255, 255, 255)  # White
ROCK_COLOR = (128, 128, 128)  # Gray
CROW_COLOR = (0, 0, 0)  # Black
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Crow and the Cup Game")

# Initialize Pygame audio
pygame.mixer.init()

# Load sound effects using PyDub
rock_drop_sound = Sine(440).to_audio_segment(duration=200)  # Example rock drop sound
crow_drink_sound = Sine(880).to_audio_segment(duration=500)  # Example crow drink sound

# Game variables
cup_water = 0
rocks_in_cup = 0
crow_thirst = 100  # Initialize crow's thirst
font = pygame.font.Font(None, 36)

def update_game_state():
    global cup_water, rocks_in_cup, crow_thirst

    # Play sound effects using Pygame
    pygame.mixer.Sound(rock_drop_sound.export(format="wav")).play()
    pygame.time.delay(200)  # Add a delay for sound effect
    pygame.mixer.Sound(crow_drink_sound.export(format="wav")).play()

    added_water = random.randint(1, 5)
    cup_water += added_water
    rocks_in_cup += 1
    crow_thirst -= added_water

def main():
    global crow_thirst

    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    update_game_state()
                if event.key == pygame.K_d:
                    if cup_water >= 20:
                        crow_thirst = 0  # Reset crow's thirst to zero

        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, CUP_COLOR, (300, 400, 200, 200))
        pygame.draw.polygon(screen, CUP_COLOR, [(300, 400), (500, 400), (400, 300)])

        pygame.draw.circle(screen, ROCK_COLOR, (450, 300), 20 * rocks_in_cup)

        pygame.draw.circle(screen, CROW_COLOR, (100, 100), 30)

        if crow_thirst <= 0:
            text = font.render("The crow is satisfied! You win!", True, (255, 255, 255))
            screen.blit(text, (150, 250))
        elif rocks_in_cup >= 20:
            text = font.render("You've stacked enough rocks, but the crow is still thirsty.", True, (255, 255, 255))
            screen.blit(text, (50, 250))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
