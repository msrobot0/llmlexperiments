import numpy as np
from scipy.io.wavfile import write

# Function to generate a sine wave with harmonics
def generate_sine_wave_with_harmonics(duration, frequency, amplitude, sample_rate, num_harmonics):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.zeros(len(t))
    for harmonic in range(1, num_harmonics + 1):
        wave += amplitude / harmonic * np.sin(2 * np.pi * frequency * harmonic * t)
    return wave

# Define parameters
sample_rate = 44100  # CD quality
duration = 1.0      # Duration of each stage (in seconds)
amplitude = 0.7
num_harmonics = 5   # Number of harmonics to add

# Define frequencies for each stage
intro_frequency = 440  # Intro
growth_frequency = 660  # Growth
flowering_frequency = 880  # Flowering
seed_production_frequency = 1100  # Seed production

# Generate audio for each stage with harmonics
intro_wave = generate_sine_wave_with_harmonics(duration, intro_frequency, amplitude, sample_rate, num_harmonics)
growth_wave = generate_sine_wave_with_harmonics(duration, growth_frequency, amplitude, sample_rate, num_harmonics)
flowering_wave = generate_sine_wave_with_harmonics(duration, flowering_frequency, amplitude, sample_rate, num_harmonics)
seed_production_wave = generate_sine_wave_with_harmonics(duration, seed_production_frequency, amplitude, sample_rate, num_harmonics)

# Concatenate the stages to represent the milkweed lifecycle
audio_data = np.concatenate((intro_wave, growth_wave, flowering_wave, seed_production_wave))

# Loop the audio for multiple lifecycle cycles
num_cycles = 3  # Number of cycles
audio_data = np.tile(audio_data, num_cycles)

# Normalize the audio
audio_data = audio_data / np.max(np.abs(audio_data))

# Write the audio to a WAV file
write("milkweed_lifecycle.wav", sample_rate, audio_data)
