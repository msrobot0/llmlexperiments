import turtle
import random

# Set up the turtle
turtle.speed(0)
turtle.bgcolor("white")
turtle.title("Sol LeWitt Inspired Art")

# Function to draw a line segment
def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Function to generate random Sol LeWitt-style art
def generate_sol_lewitt_art(num_lines, canvas_size):
    for _ in range(num_lines):
        x1 = random.randint(-canvas_size, canvas_size)
        y1 = random.randint(-canvas_size, canvas_size)
        x2 = random.randint(-canvas_size, canvas_size)
        y2 = random.randint(-canvas_size, canvas_size)

        draw_line(x1, y1, x2, y2)

# Set the number of lines and canvas size
num_lines = 50
canvas_size = 300

# Generate Sol LeWitt-inspired art
generate_sol_lewitt_art(num_lines, canvas_size)

# Close the drawing window when clicked
turtle.exitonclick()

