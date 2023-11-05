import turtle
import random

# Set up the turtle
turtle.speed(0)
turtle.bgcolor("white")
turtle.title("Cy Twombly Inspired Art")

# Function to create Cy Twombly-inspired art
def create_cy_twombly_inspired_art():
    for _ in range(100):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        for _ in range(20):
            turtle.pencolor(random.random(), random.random(), random.random())
            turtle.forward(random.randint(10, 50))
            turtle.right(random.randint(-180, 180))

# Generate Cy Twombly-inspired art
create_cy_twombly_inspired_art()

# Close the drawing window when clicked
turtle.exitonclick()

