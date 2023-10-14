# Current Experiments: Generate audio-visual python code from chat gpt 

I have been really inspired by the ability of LLMs to generate code. I plan to download an open source model from hugging face and use that but right now I just want to get started so I am using Chat GPT. 

This is the beginning of the experiment so I am going slow and I dont know where this is going. 

## Daily Experiment

In  my musical work I have been working with synthesizers for a while with my on-again-off-again band. We call what we do making beeps and bloops. I have been listening to a lot of drone, ambient, brian eno, you get the picture. What can a synth do that a more traditional instrument cannot. What is a traditional instrument? I have to define that - but it is related to somehow to generating music from a gesture - and yes I know synths and turning knobs are gestural - I am still working out this idea. 

I am using analog syths sometimes so I dont want to do the analog/binary distinction. 

With a synth you have granular control over the audio frequency and the generation of sound. At somepoint I'll talk more about this. But for now I am going to cryptically say that sound becomes 'unbundled' from gesture. Maybe even from performance. 

So again I ask what can a synth do that a traditional intrument cannot.

Two thoughts come to my mind: 
1) What is it like to live inside a note
2) What is it like to have a note without a beginning and an end. 


Today, and probably in the future, I am exploring the idea of living inside a note through the concept of microtones. that is very slight frequency variations  on a western traditional concept of a note.  Non-european cultures (and probably folk european traditions) use microtones, but the degree of granularity we can get with a synth is beyond anything we can name in any culture that names notes  because naming is discrete and countable, and microtones are continuous and non-countable.

## Audio: Prompt and Code 
>generate audio in python that explores the microtones if bflat with a syncopated drone


To generate audio in Python that explores microtones of B-flat with a syncopated drone, you can use the `pydub` library to create audio and incorporate a syncopated rhythm pattern. Here's an example of how to achieve this:

First, install the `pydub` library if you haven't already:

```bash
pip install pydub
```

Now, you can create a Python script to generate the audio:

```python
from pydub import AudioSegment
import random

# Define the base frequency for B-flat (in Hz)
base_frequency = 466.16  # Adjust this as needed

# Create an empty audio segment
audio = AudioSegment.silent(duration=60000)  # 60 seconds

# Generate a syncopated rhythm pattern
rhythm_pattern = [random.choice([0, 0, 1]) for _ in range(600)]  # Adjust the length as needed

# Generate audio with microtonal variations and syncopation
for i in range(len(rhythm_pattern)):
    if rhythm_pattern[i] == 1:
        microtone = base_frequency * (2 ** (random.uniform(-0.02, 0.02)))
        duration = 100  # Adjust the duration of each note
        note = AudioSegment.sine(duration=duration, frequency=microtone)
        audio = audio.overlay(note)

# Export the audio to a file
audio.export("microtonal_bflat_syncopated_drone.wav", format="wav")
```

In this code:

- We define a base frequency for B-flat and create an empty audio segment.
- We generate a syncopated rhythm pattern using a list of 0s and 1s. You can adjust the length of the pattern as needed.
- Within the loop, we create microtonal variations of B-flat by multiplying the base frequency with random values within a small range.
- We create short notes for each "1" in the rhythm pattern and overlay them onto the audio segment.
- Finally, we export the generated audio to a WAV file.

You can adjust the parameters such as note duration, rhythm pattern length, and microtonal range to create the desired audio composition with microtones of B-flat and syncopation.


## The Audio Code Analysis

The code  chat gpt generated did not work. I had to look up the undocumented sine functionality in pydub - which I had never used - and replace the ml generated code with something that worked. It was not much work - I did it in under 10 minutes. However the result was underwelming. I wanted to generate a 5 second piece and this was like a 1 second piece with 4 minutes of silence - very goddard but that was not what I was going for. It was acutally funny because Quiet City by Copeland would play after my audio sample and at first i thought it was my audio sample and marveled at the genius of my ml collaboration - until I realized no this was Aaron Copeland- it is beautiful and etherial I do suggest you listen to it however.

You can listen to it in this repository.

## Video: Prompt and Code 
>    now code a python generative animation in bluetones using organic shapes and transparency that represents the audio generation above

>Creating a generative animation in Python to represent the audio generation can be done using libraries like Pygame. Here's a simple example that generates organic shapes with transparency to accompany the audio:

First, you need to install Pygame:

```bash
pip install pygame
```

Now, create a Python script for the generative animation:

```python
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Generative Animation")

# Define colors with transparency
transparent_blue = (0, 0, 255, 128)
transparent_green = (0, 255, 0, 128)

# Create a clock to control frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Generate organic shapes
    for _ in range(10):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(10, 50)
        rotation = random.randint(0, 360)
        transparency = random.randint(50, 200)
        color = transparent_blue if random.random() < 0.5 else transparent_green

        # Create organic shape
        surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, color, (radius, radius), radius)
        surface = pygame.transform.rotate(surface, rotation)

        screen.blit(surface, (x, y))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(30)

pygame.quit()
```
OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com

In this code:

- We use Pygame to create the animation with organic shapes (circles) that have transparency (using the `SRCALPHA` flag).
- The shapes are randomly positioned, rotated, and given transparency. The color alternates between transparent blue and transparent green.
- The animation is displayed on the screen, and the frame rate is controlled with the clock to achieve a smoother animation.

This code is a simple example, and you can modify it to create more complex and organic shapes or patterns that represent the audio generated in the previous step.

## The Video Code Analysis
This also did not work at first. I had to import ImageFrame from PIL, the python image library, and then comment out a line of audio code that called a non-existant audio reader. 

While in the code I could not help myself by making a few tweaks. 
I got the framerate down so it felt less jumpy, I increased the number of dust motes and the size of the dust motes so they would overlap more, I also made the length and width absolutely different sizes which I think contributes to the feeling like this is a broken television set from the 1950-80s.  I would have liked to have this be more obviously blue and for the grayscale to be less pixelated and more transparent but this may be an effect or pygame - the library used to generate the video. 

The audio and video together did not work properly. I could not hear the audio in quicktime and then in video lan client (VLC) I could not play the video smoothly.  As I result I generated a new mp4 from the video and audio using fffmpeg (and not chat gpt)  

ffmpeg -i dust_motes_and_clouds.mp4 -i microtonal_bflat_syncopated_drone_5s.wav -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac -b:a 192k output.mp4

## Conclusion 
This was fun and took way more time than I had expected. I hope to turn this into a daily practice but I hope it will be a bit faster. 

### stack 
vim, osx, obsidian, chrome

### next steps
-more prompt engineering
-use an open source model
-run an open source model locally
-train an open source model on my own data
-I also just got it in my head to use LLMs to generate speech acts. Not sure what that would be but I'm reading lots of performance theory these days 
-spell check and grammar check my write ups  

### addendum 
- I asked chat gpt to "improve this writing by making it more engaging and readble with better grammar and spelling". - read the result here
