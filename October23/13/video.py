import random
import numpy as np
import imageio_ffmpeg as ffmpeg
from moviepy.editor import VideoClip
from PIL import Image, ImageDraw

# Set the video parameters
width, height = 800, 600
frame_rate = 30
duration = 5  # Video duration in seconds

# Create a function to generate frames
def generate_frame(t):
    # Create a new frame
    frame = Image.new("RGBA", (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(frame)

    # Generate organic shapes
    for _ in range(10):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(10, 50)
        rotation = random.randint(0, 360)
        transparency = random.randint(50, 200)
        color = (0, 0, 255, transparency) if random.random() < 0.5 else (0, 255, 0, transparency)

        # Create organic shape
        theta = np.linspace(0, 2 * np.pi, 100)
        x_coords = [x + radius * np.cos(angle) for angle in theta]
        y_coords = [y + radius * np.sin(angle) for angle in theta]
        
        # Convert coordinates to tuples
        xy = [(int(x_coords[i]), int(y_coords[i])) for i in range(100)]
        
        # Draw the lines
        draw.line(xy, fill=color, width=2)

    return np.array(frame)

# Generate the video
video = VideoClip(generate_frame, duration=duration)

# Load and synchronize the audio
audio = VideoFileClip("microtonal_bflat_syncopated_drone_5s.wav")
video = video.set_audio(audio)

# Write the video to a file
video.write_videofile("generative_animation.mp4", codec="libx264", fps=frame_rate)

# Close the audio file
audio.reader.close_proc()

# Close the video file
video.reader.close()

# Free up resources
video.close()
audio.close()
