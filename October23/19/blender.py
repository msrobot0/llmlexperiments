import bpy
import math
import random

# Clear the default scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Set up the Möbius strip
bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
mobius_strip = bpy.context.object
mobius_strip.modifiers.new(name="Twist", type='SIMPLE_DEFORM')
mobius_strip.modifiers['Twist'].deform_method = 'TWIST'
mobius_strip.modifiers['Twist'].factor = 1.0
mobius_strip.modifiers['Twist'].angle = 6.28319  # 360 degrees in radians

# Create the ball
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(0, 0, 0.1))
ball = bpy.context.object

# Create a camera
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(3, -3, 2))
camera = bpy.context.object
bpy.context.scene.camera = camera

# Set up lighting
bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD', location=(1, -1, 3))
light = bpy.context.object

# Set up animation
frame_start = 1
frame_end = 250
bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end

for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)

    # Animate the ball's position along the Möbius strip
    ball.location.x = 1.0 * math.cos(frame * 0.1)
    ball.location.y = 1.0 * math.sin(frame * 0.1)

    ball.keyframe_insert(data_path="location")

# Apply vaporwave-style materials and lighting
mobius_strip.data.materials.append(bpy.data.materials['Vaporwave_Material'])
ball.data.materials.append(bpy.data.materials['Vaporwave_Ball_Material'])
light.data.energy = 2.0
light.data.color = (0.8, 0.2, 0.8, 1)

# Set up rendering
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.image_settings.color_mode = 'RGBA'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'
bpy.context.scene.render.filepath = 'output.mp4'

# Render the animation
bpy.ops.render.render(animation=True)


