import numpy as np
from PIL import Image, ImageDraw
import random
from moviepy.editor import VideoClip, AudioFileClip
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Set the video parameters
width, height = 800, 600
frame_rate = 10
duration = 5  # Video duration in seconds

# Function to generate frames
def generate_frame(t):
    # Create a new frame
    frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    # Generate animated dust motes and clouds in shades of blue
    num_dust_motes = 400
    for q in range(num_dust_motes):
        transparency = random.randint(100, 250)
        blue_color = (random.randint(0,50), random.randint(0,50), 255, transparency)
        x, y = random.randint(0, width), random.randint(0, height)
        sizex = random.randint(50, random.randint(0,width)+100)
        sizey = random.randint(1, random.randint(0,height)+50)
        draw = ImageDraw.Draw(frame)
        draw.ellipse([x, y, x + sizex, y + sizey], fill=blue_color)

    return np.array(frame)

# Generate the video
video = VideoClip(generate_frame, duration=duration)

# Load and synchronize the audio (replace with your B flat audio)
#audio = AudioFileClip("microtonal_bflat_syncopated_drone_5s.wav")
#video = video.set_audio(audio)
print("here")

# Write the video to a file
#video.write_videofile("dust_motes_and_clouds.mp4", codec="libx264", fps=frame_rate)

# Close the audio file
#audio.reader.close_proc()

video.write_videofile("dust_motes_and_clouds.mp4", 
                     codec='libx264', 
                     audio_codec='wav', 
                     temp_audiofile='microtonal_bflat_syncopated_drone_5s.wav', 
                     remove_temp=False,
                     fps=frame_rate,
                     )

# Close the video file
video.close()
print("saved this file as dust_motes_and_clouds.mp4")
# Display the video
#video.ipython_display(fps=frame_rate)
