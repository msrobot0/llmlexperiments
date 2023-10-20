from vpython import *

# Create the 3D scene
scene = canvas(title="Volcano Simulation", width=800, height=600)

# Create a simple volcano cone
volcano_cone = cone(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=5, color=color.red)

# Create a lava flow
lava = cylinder(pos=vector(0, 0, 0), axis=vector(0, 5, 0), radius=0, color=color.orange)

# Create a ground plane
ground = box(pos=vector(0, -5, 0), length=20, height=0.1, width=20, color=color.green)

# Simulation loop
t = 0
dt = 0.01
while True:
    rate(100)  # Adjust the frame rate as needed

    # Make the lava flow down
    lava.pos.y -= 0.1
    t += dt

    # Restart lava flow when it reaches the ground
    if lava.pos.y < ground.pos.y:
        lava.pos.y = 0
        t = 0

