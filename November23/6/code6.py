import turtle

# Initialize the turtle
heart = turtle.Turtle()
turtle.bgcolor("white")
heart.speed(1)
heart.color("red")
heart.pensize(5)

# Draw a heart shape
heart.begin_fill()
heart.fillcolor("red")
heart.left(50)
heart.forward(133)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.forward(133)
heart.end_fill()

# Add a text message
heart.penup()
heart.color("black")
heart.goto(0, -50)
heart.write("Healing", align="center", font=("Arial", 20, "normal"))

# Animation function
def animate_heart():
    for i in range(4):
        heart.fillcolor("white")
        heart.begin_fill()
        heart.left(90)
        heart.fillcolor("red")
        heart.end_fill()
        heart.fillcolor("white")
        heart.begin_fill()
        heart.fillcolor("red")
        heart.end_fill()

# Animate the heart to symbolize healing
for _ in range(5):
    animate_heart()

# Close the window on click
turtle.exitonclick()

