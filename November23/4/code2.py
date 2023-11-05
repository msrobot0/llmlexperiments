import matplotlib.pyplot as plt
import random

# Function to generate random Sol LeWitt-style art
def generate_sol_lewitt_art(num_lines, canvas_size):
    plt.figure(figsize=(6, 6))
    for _ in range(num_lines):
        x1 = random.randint(-canvas_size, canvas_size)
        y1 = random.randint(-canvas_size, canvas_size)
        x2 = random.randint(-canvas_size, canvas_size)
        y2 = random.randint(-canvas_size, canvas_size)

        plt.plot([x1, x2], [y1, y2], color='black')

    plt.xlim(-canvas_size, canvas_size)
    plt.ylim(-canvas_size, canvas_size)
    plt.axis('off')
    plt.show()

# Set the number of lines and canvas size
num_lines = 50
canvas_size = 300

# Generate Sol LeWitt-inspired art
generate_sol_lewitt_art(num_lines, canvas_size)

