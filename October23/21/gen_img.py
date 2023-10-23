import os
from PIL import Image, ImageDraw, ImageFont

# Directory to store image files
output_directory = "milkweed_lifecycle_images"
os.makedirs(output_directory, exist_ok=True)

# Parameters
frame_width = 1920
frame_height = 1080

# Function to create an image for a specific stage
def create_image_for_stage(stage, frame_width, frame_height):
    image = Image.new("RGB", (frame_width, frame_height), color="white")
    draw = ImageDraw.Draw(image)

    # Set font and text properties
    font = ImageFont.load_default()
    text = f"Stage: {stage}"
    text_width, text_height = draw.textsize(text, font)
    text_position = ((frame_width - text_width) / 2, (frame_height - text_height) / 2)
    text_color = "black"

    draw.text(text_position, text, fill=text_color, font=font)

    return image

# List of stages (you can customize this)
stages = ["Intro", "Growth", "Flowering", "Seed Production"]

# Generate image files for each stage
for i, stage in enumerate(stages):
    image = create_image_for_stage(stage, frame_width, frame_height)
    image_filename = os.path.join(output_directory, f"stage_{i+1}.png")
    image.save(image_filename)

# Print a message to confirm image creation
print(f"Generated {len(stages)} image files in the '{output_directory}' directory.")

