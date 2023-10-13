# Current Experiments: Generating Audio-Visual Python Code with Chat GPT

I've recently been profoundly inspired by the capabilities of large language models (LLMs) in generating code. My plan involves downloading an open-source model from Hugging Face, but for now, I'm excited to start this journey by utilizing Chat GPT.

This marks the inception of an experimental venture, and as I take these initial steps, I'm fully aware that I'm embarking on an unknown path.

## Daily Experiment

In my musical endeavors, I've been working with synthesizers for quite some time, often collaborating with my on-and-off band. We affectionately refer to our musical style as "making beeps and bloops." Lately, my auditory landscape has been filled with drone music, ambient sounds, and the works of artists like Brian Eno. It's got me thinking deeply about what synthesizers can achieve that traditional instruments cannot. 

Defining what constitutes a "traditional" instrument is a task in itself. It relates to the idea of generating music from gestures, and while I recognize that working with synthesizers and twisting knobs is a form of gestural expression, I'm still exploring this concept.

I occasionally use analog synths, and I'm avoiding the binary/analog dichotomy, as it doesn't fully capture the essence of what's possible.

What's truly compelling about synths is the degree of control they offer over audio frequencies and sound generation. This level of granularity allows for experimentation that I'll delve into further at some point. For now, I'll cryptically hint that sound becomes 'unbundled' from gesture, and perhaps even from traditional forms of musical performance.

So, here's my central question: What unique capabilities do synthesizers possess that set them apart from traditional instruments?

Two particular thoughts intrigue me:

1) What does it feel like to exist within a single musical note?
2) What's the experience of a note that has no clear beginning or end?

In today's experiment, and likely in many more to come, I'm delving into the idea of "living inside a note" through the concept of microtones. Microtones represent slight frequency variations within the framework of the Western musical note. While non-European cultures, and perhaps various folk traditions in Europe, embrace microtones, the level of granularity achievable with a synth transcends any known musical system. This is because microtones are continuous and defy conventional quantification, in contrast to the discrete and countable nature of traditionally named notes.

## Audio: Prompt and Code

Now, let's explore the creation of audio in Python that delves into the realm of microtonal B-flat with a syncopated drone. This audio generation will be complemented by a generative animation using Python.

## Generative Animation with Pygame

To create a generative animation that represents the audio generation, we'll harness the power of Pygame, a popular library. But before we dive in, make sure to install Pygame:

```bash
pip install pygame
```

Now, let's craft the Python script for our generative animation:

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
        pygame.draw circle(surface, color, (radius, radius), radius)
        surface = pygame.transform.rotate(surface, rotation)

        screen.blit(surface, (x, y))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(30)

pygame.quit()
```

In this code:

- We're utilizing Pygame to craft an animation enriched with organic shapes, primarily circles. These shapes possess a level of transparency, thanks to the `SRCALPHA` flag.
- These organic shapes are randomly placed, rotated, and given a degree of transparency. The color choice alternates between transparent blue and transparent green.
- The animation is

 showcased on the screen, and the frame rate is governed by the clock to ensure a smoother viewing experience.

This code serves as a starting point. You can expand and modify it to create more intricate and captivating visuals to accompany your audio creation.

## The Audio Code Analysis

The code generated by Chat GPT didn't perform as expected. I had to explore and discover undocumented features, such as the sine functionality in Pydub, which I hadn't previously used. Eventually, I replaced the machine learning-generated code with something functional. It was a relatively straightforward process, taking less than 10 minutes. However, the result was somewhat underwhelming. My intention was to generate a 5-second audio piece, but what I obtained was more like a 1-second piece with 4 minutes of silence. It was quite avant-garde, reminiscent of Godard, but not the effect I was aiming for. Interestingly, after my audio sample, Aaron Copland's "Quiet City" started playing. At first, I thought it was part of my audio sample and marveled at the apparent genius of my AI collaboration. It was only later that I realized the beautiful, ethereal music was Aaron Copland's work. I highly recommend giving it a listen, although it was not what I initially intended.

## Video: Prompt and Code

Now, let's embark on the journey of creating a Python generative animation in blue tones, using organic shapes and transparency to represent the audio generation.

## Creating the Generative Animation

To craft a generative animation that mirrors the audio generation, we can employ libraries like Pygame. Here's a simple example to get you started:

1. First, make sure to install Pygame:

```bash
pip install pygame
```

2. Now, let's create a Python script for the generative animation:

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

In this code:

- We use Pygame to create the animation, featuring organic shapes (circles) with transparency using the `SRCALPHA` flag.
- The organic shapes are randomly placed, rotated, and given a degree of transparency. The choice of color alternates between transparent blue and transparent green.
- The animation is displayed on the screen, and the frame rate is controlled with the clock for a smoother visual experience.

This code provides a foundation, and you're welcome to adapt and enhance it to create more complex and captivating visuals that complement the audio generated earlier.

## The Video Code Analysis

While implementing the video generation, I encountered some initial challenges. I had to import `ImageFrame` from the Python Imaging Library (PIL) and comment out a line of audio code that referred to a non-existent audio reader.

During the process, I couldn't resist making a few tweaks. I reduced the framerate to create a smoother appearance, increased the number and size of dust motes to enhance their overlap, and intentionally distorted the aspect ratio, giving the impression of a vintage television set from the 1950s to 1980s. While I wished for a more distinct blue tone and smoother transparency in grayscale, the final result may have been influenced by the properties of Pygame, the library used to create the video.

Unfortunately, the combination of audio and video didn't perform seamlessly. I couldn't hear the audio in QuickTime, and playing the video in VLC (VideoLAN Client) proved to be somewhat challenging. Consequently, I took the initiative to generate a new MP4 file by merging the video and audio using FFmpeg, bypassing Chat GPT:

```bash
ffmpeg -i dust_motes_and_clouds.mp4 -i microtonal_bflat_syncopated_drone_5s.wav -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac -b:a 192k output.mp4
```

## Conclusion

This experimental journey proved to be both enjoyable and more time-consuming than anticipated. My hope is to turn this into a daily practice, with the expectation that it becomes more efficient in the future. It's all part of the creative process and a testament to the dynamic world of art and technology.

OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com