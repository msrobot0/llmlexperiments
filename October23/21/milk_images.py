import numpy as np
import os
import subprocess
from PIL import Image

# Directory to store image files
output_directory = "milkweed_lifecycle_images"
os.makedirs(output_directory, exist_ok=True)

# Parameters
frame_width = 1920
frame_height = 1080
frame_rate = 30
duration_per_stage = 3  # Adjust as needed

# Function to create an image for a specific stage
def create_image_for_stage(stage, frame_width, frame_height):
    # Placeholder: Create a blank image with the stage name
    image = Image.new("RGB", (frame_width, frame_height))
    return np.array(image)

# List of stages (you can customize this)
stages = ["Intro", "Growth", "Flowering", "Seed Production"]

# Generate image files for each stage
for i, stage in enumerate(stages):
    image = create_image_for_stage(stage, frame_width, frame_height)
    image_filename = os.path.join(output_directory, f"stage_{i+1}.png")
    Image.fromarray(image).save(image_filename)

# Generate the video using ffmpeg-python
input_pattern = os.path.join(output_directory, "stage_%d.png")
output_filename = "milkweed_lifecycle.mp4"

# Create a list of arguments for FFmpeg
ffmpeg_args = [
    "ffmpeg",
    "-framerate", str(frame_rate),
    "-i", input_pattern,
    "-c:v", "libx264",
    "-r", str(frame_rate),
    output_filename
]

# Execute the FFmpeg command
subprocess.run(ffmpeg_args)

# Clean up: Remove the temporary image files
for i in range(len(stages)):
    image_filename = os.path.join(output_directory, f"stage_{i+1}.png")
    os.remove(image_filename)
