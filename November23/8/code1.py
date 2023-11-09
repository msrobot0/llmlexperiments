import numpy as np

def adsr_envelope_generator(attack_time, decay_time, sustain_level, release_time, total_time, sample_rate):
    """
    Generate an ADSR envelope.

    Args:
        attack_time (float): Time in seconds for the attack phase.
        decay_time (float): Time in seconds for the decay phase.
        sustain_level (float): Sustain level (0 to 1).
        release_time (float): Time in seconds for the release phase.
        total_time (float): Total duration of the envelope.
        sample_rate (int): Sampling rate in Hz.

    Returns:
        np.ndarray: An array containing the generated ADSR envelope.
    """
    num_samples = int(total_time * sample_rate)
    t = np.linspace(0, total_time, num_samples, endpoint=False)

    # Generate the envelope stages
    attack_samples = int(attack_time * sample_rate)
    decay_samples = int(decay_time * sample_rate)
    release_samples = int(release_time * sample_rate)

    envelope = np.zeros(num_samples)
    envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    envelope[attack_samples:attack_samples + decay_samples] = np.linspace(1, sustain_level, decay_samples)
    envelope[-release_samples:] = np.linspace(sustain_level, 0, release_samples)

    return envelope

# Example usage
import matplotlib.pyplot as plt

attack_time = 0.1
decay_time = 0.2
sustain_level = 0.6
release_time = 0.3
total_time = 2.0
sample_rate = 44100

envelope = adsr_envelope_generator(attack_time, decay_time, sustain_level, release_time, total_time, sample_rate)

# Plot the ADSR envelope
plt.figure()
plt.title("ADSR Envelope")
plt.plot(envelope)
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.show()
