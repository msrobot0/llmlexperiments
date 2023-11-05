import turtle
import random

# Set up the turtle
turtle.speed(0)
turtle.bgcolor("white")
turtle.title("Jackson Pollock Inspired Art")

# Function to create Jackson Pollock-inspired art
def create_jackson_pollock_inspired_art():
    for _ in range(1000):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        for _ in range(10):
            turtle.pencolor(random.random(), random.random(), random.random())
            turtle.dot(random.randint(1, 5))
            turtle.forward(random.randint(1, 10))
            turtle.right(random.randint(0, 360))

# Generate Jackson Pollock-inspired art
create_jackson_pollock_inspired_art()

# Close the drawing window when clicked
turtle.exitonclick()

