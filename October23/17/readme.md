Day 5 of the LLM Experiments - I am sort of sticking this in to the end of my day, like a rushed cup of coffee or push ups and sit ups between meetings. But each experiment i do teaches me something new - to make a truly banal comment.

I am thinking about creating a format for these writeups so they are less idiosycratic -but I am not doing that today.  The code is aavailable on [Githib](https://github.com/msrobot0/llmlexperiments/tree/main/October23/17)  along with animations and photos. 


![[videogame.mov]]

Today I started out trying to generate music again. My music experiments dont really turn out - often time a wav form is not generated.   I did a prompt to improvise on chants of japji - the sikh chant - I got something in korean via google translate. Which was strange. It made me think about doing an audio piece with many different languages. But text to speech sounds pretty bad. We need some FFTs or something to add some personality. 

I decided to prompt the LLM to make a game. This is new and visual
![[image.png]]

It is based on the aesop fable the crow and the pitcher. The crow adds pebbles to a pitcher of water -as the stones are added - the water rises and the crow can then drink the pitcher. 

Lots of fables and fairytales feel like they have video game logic to me. 

## Promp

> generate a game in python where the player tries to stack rocks in a cup so that a crow can drink the water in the cup like the aesop fable crow and pitcher

## output
Creating a Python game where the player attempts to stack rocks in a cup for a crow to drink the water, inspired by Aesop's fable "The Crow and the Pitcher," is a fun project. Here's a simple text-based version of such a game:

```python
import random

# Initialize game variables
cup_water = 0
rocks_in_cup = 0
crow_thirst = 100
game_over = False

print("Welcome to 'The Crow and the Cup' Game!\n")
print("The crow is thirsty, and you need to stack rocks in the cup to raise the water level.")

while not game_over:
    print("\nOptions:")
    print("1. Stack a rock in the cup")
    print("2. Let the crow drink")
    print("3. Quit the game")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        added_water = random.randint(1, 5)
        cup_water += added_water
        rocks_in_cup += 1
        crow_thirst -= added_water
        print(f"You added {added_water} units of water to the cup. The crow's thirst is now {crow_thirst}.")
    elif choice == "2":
        if cup_water >= 20:
            print("The crow is happy and quenched its thirst! You win!")
            game_over = True
        else:
            print("The water level is too low for the crow to drink. Keep stacking rocks.")
    elif choice == "3":
        print("You quit the game. The crow is still thirsty.")
        game_over = True
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

    # Check for crow's condition
    if crow_thirst <= 0:
        print("The crow's thirst reached zero. The crow is satisfied, and you win!")
        game_over = True
    elif rocks_in_cup >= 20:
        print("You've stacked enough rocks, but the crow is still thirsty. You didn't add enough water.")
        game_over = True

print("Thanks for playing 'The Crow and the Cup' Game!")
```

In this text-based game, you have three options: adding rocks to the cup, allowing the crow to drink, or quitting the game. The goal is to stack enough rocks to raise the water level so the crow can quench its thirst. If you successfully raise the water level to 20 units or satisfy the crow's thirst, you win the game.

You can expand this game by adding a graphical interface, more complex mechanics, and visual elements to make it more engaging.
OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com

## Comment 
![[crowandcup.png]]

The output was a text based game. Something I did not expect. I was really surprised  and inspired. It made me want to experiment more in this genre - or maybe specify a package like twine. 

This also does have game logic your goal is to add enough rocks so that the crow can drink before it dies. 

But I wanted an audio visual experience
## Prompt 
>  
make the game a video animation

>please add some generated sound effects

## Code

import pygame
import random
import sys
from pydub import AudioSegment
from pydub.generators import Sine

# Initialize Pygame
pygame.init()

# Initialize PyDub audio
pygame.mixer.init()

# Constants
# (Your previous constants here...)

# Load sound effects using PyDub
rock_drop_sound = Sine(440).to_audio_segment(duration=200)  # Example rock drop sound
crow_drink_sound = Sine(880).to_audio_segment(duration=500)  # Example crow drink sound

# Game variables
# (Your previous game variables here...)

def update_game_state():
    global cup_water, rocks_in_cup, crow_thirst

    # Generate sound effects
    rock_drop_sound.play()
    pygame.time.delay(200)  # Add a delay for sound effect
    crow_drink_sound.play()

    added_water = random.randint(1, 5)
    cup_water += added_water
    rocks_in_cup += 1
    crow_thirst -= added_water

# (Your previous code here...)

def main():
    # (Your previous code here...)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    update_game_state()
                if event.key == pygame.K_d:
                    if cup_water >= 20:
                        crow_thirst = 0

        # (Your previous code here...)

if __name__ == "__main__":
    main()

import pygame
import random
import sys
from pydub import AudioSegment
from pydub.generators import Sine

# Initialize Pygame
pygame.init()

# Initialize PyDub audio
pygame.mixer.init()

# Constants
# (Your previous constants here...)

# Load sound effects using PyDub
rock_drop_sound = Sine(440).to_audio_segment(duration=200)  # Example rock drop sound
crow_drink_sound = Sine(880).to_audio_segment(duration=500)  # Example crow drink sound

# Game variables
# (Your previous game variables here...)

def update_game_state():
    global cup_water, rocks_in_cup, crow_thirst

    # Generate sound effects
    rock_drop_sound.play()
    pygame.time.delay(200)  # Add a delay for sound effect
    crow_drink_sound.play()

    added_water = random.randint(1, 5)
    cup_water += added_water
    rocks_in_cup += 1
    crow_thirst -= added_water

# (Your previous code here...)

def main():
    # (Your previous code here...)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    update_game_state()
                if event.key == pygame.K_d:
                    if cup_water >= 20:
                        crow_thirst = 0

        # (Your previous code here...)

if __name__ == "__main__":
    main()


### comment
I had to do some debugging on this - there were global variables that were not defined and other issues. But I do have an audio visual experience and I ppress the s and d keys and something happens. I am not sure if there is game logic. It is not apparent from playing the game I have to look in the code. 

I am sort of inspired by the text element however I am going to explore that more in the future. 

GN