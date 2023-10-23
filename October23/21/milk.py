import numpy as np
from scipy.io.wavfile import write

# Function to generate a sine wave
def generate_sine_wave(duration, frequency, amplitude, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave

# Define parameters
sample_rate = 44100  # CD quality
duration = 1.0      # Duration of each stage (in seconds)
amplitude = 0.7

# Define frequencies for each stage
intro_frequency = 440  # Intro
growth_frequency = 660  # Growth
flowering_frequency = 880  # Flowering
seed_production_frequency = 1100  # Seed production

# Generate audio for each stage
intro_wave = generate_sine_wave(duration, intro_frequency, amplitude, sample_rate)
growth_wave = generate_sine_wave(duration, growth_frequency, amplitude, sample_rate)
flowering_wave = generate_sine_wave(duration, flowering_frequency, amplitude, sample_rate)
seed_production_wave = generate_sine_wave(duration, seed_production_frequency, amplitude, sample_rate)

# Concatenate the stages to represent the milkweed lifecycle
audio_data = np.concatenate((intro_wave, growth_wave, flowering_wave, seed_production_wave))

# Normalize the audio
audio_data = audio_data / np.max(np.abs(audio_data))

# Write the audio to a WAV file
write("milkweed_lifecycle.wav", sample_rate, audio_data)

