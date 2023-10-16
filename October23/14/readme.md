# Experiment number 2.

It is said that aikido, the martial art, was   
Morihei Ueshiba gift when he awakened.  I believe Tai Chi, which I have practiced on and off for 16 years was also brought to the world in a similar way. Guru Nanak, the founder of Sikhism, was gifted the poem [Japji](https://www.youtube.com/watch?v=uuAPRAydzqg).  There are many stories of visionary gifts people receive when they awaken. As I understand it, to awaken means to awaken into a unity consciousness, to lose the myth that we are separate with control over anything. With this awareness all of our actions become as natural and full of integrity as the heart beat. 

So this morning I had all these things in my mind. If we all were awakened there would be no more violence - although there would still be disagreements , people would irritate one another.  I have thought before about asking an LLM for a protocol for awakening, moksha, etc or for creating new somatic practices. This morning I decided to ask the LLM to create a diagram for dancing.

I have been going through a performance studies rabbit hole since reading Barbara Brownings 'The Gift' a few weeks ago - and ths along with dance diagrams are in my head.  Here are some [examples](https://www.pinterest.com/rexxer/bodymovement-diagrams/) on [pinterest](https://www.pinterest.com.au/pin/283656476511044732/)

![[Pasted image 20231014140442.png]]

from: https://www.researchgate.net/publication/296469156_Dance_Music_Meter_and_Groove_A_Forgotten_Partnership

So I went through a bunch of different prompts. 
First I generated an svg file -  The SVG file was boring - I figured let me generate a python script to generate the svg file because then at least I couold edit that. I am better with python than with SVG.  

# WHY SVG
I figured it would be easy to create images that we could print with a plotter - but that is a post for another time. 

## Prompt 1
Prompt: generate animated diagrams using gray scale, many lines, arrows, and bezier curves like dance step dagrams , to create a dance to end violence among humans and promote peace

> Creating a detailed animated dance step diagram for a dance aimed at promoting peace and ending violence is a complex task. However, I can provide you with a more complex textual representation of a simplified example using SVG, including grayscale lines, arrows, and Bezier curves. This example represents just a small part of a dance sequence and can serve as a starting point for creating a more elaborate diagram:

```xml
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">

    <!-- Background -->
    <rect x="0" y="0" width="400" height="400" fill="white" />

    <!-- Dance Step Diagram -->
    <path d="M100 200 Q150 100 200 200 T300 200 Q350 100 400 200" stroke="gray" stroke-width="2" fill="none">
        <animate attributeName="d" from="M100 200 Q150 100 200 200 T300 200 Q350 100 400 200" to="M100 200 Q150 300 200 200 T300 200 Q350 300 400 200" dur="4s" begin="0s" repeatCount="indefinite" />
    </path>

    <!-- Arrows -->
    <polygon points="195,205 215,195 215,215" fill="gray">
        <animate attributeName="points" from="195,205 215,195 215,215" to="195,205 215,215 215,195" dur="4s" begin="0s" repeatCount="indefinite" />
    </polygon>
    <polygon points="405,205 425,195 425,215" fill="gray">
        <animate attributeName="points" from="405,205 425,195 425,215" to="405,205 425,215 425,195" dur="4s" begin="0s" repeatCount="indefinite" />
    </polygon>

    <!-- Additional Lines or Steps -->
    <!-- Add more lines, curves, and arrows to represent various dance steps. -->

</svg>
```

This example shows a dance step sequence with a Bezier curve and directional arrows. To create a full dance sequence aimed at promoting peace and ending violence, you would need to define a series of steps with intricate movements and transitions, adding more lines, curves, and arrows as needed. 

For a comprehensive and professional dance step diagram, it's recommended to use dedicated graphic design software and collaborate with a skilled graphic designer or choreographer who can create detailed and meaningful diagrams for your specific dance concept.

OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com

I think this is the example in the repository under example1. I wanted to add more circles and lines and arrows but again my svg knowledge is limited.  I am going to use this perhaps as an opportunity to expand it.

# Prompt 2
prompt: write a python program using the xml ibrary to generate an animated diagram in svg using gray scale, more than 20 lines, the lines have arrows and bezier curves like dance step diagrams , to create a dance to end violence among humans and promote peace and save this as a mov

This was after a few prompts where LLM gave me cairosvg and svgwriter -neither of which I could get to work, so told it to use the xml library to generate the svg. 

> Creating a complex animated diagram with over 20 lines, arrows, and Bezier curves in SVG and then converting it into a MOV (QuickTime) file directly in Python is a substantial task. It typically involves a combination of graphic design, animation, and video editing software. 

For creating the SVG diagram, you can use the `xml.etree.ElementTree` library to generate SVG content, as demonstrated in the following Python program. However, for converting the SVG to MOV, you'll need to use external video editing software or a library that specializes in video creation (e.g., `ffmpeg-python`).

Here's a Python program that generates a simplified SVG diagram with a few lines and Bezier curves, along with arrows:

```python
import xml.etree.ElementTree as ET

# Create SVG root element
root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", width="400", height="400")

# Create definitions for the arrowhead marker
defs = ET.SubElement(root, "defs")
marker = ET.SubElement(defs, "marker", id="arrowhead", markerWidth="10", markerHeight="7", refX="0", refY="3.5", orient="auto")
polygon = ET.SubElement(marker, "polygon", points="0 0, 10 3.5, 0 7", fill="gray")

# Create paths with arrows and Bezier curves
for i in range(20):
    path = ET.SubElement(root, "path", d=f"M{i*20} 200 Q{i*20+50} 100 {i*20+100} 200", stroke="gray", stroke_width="2", fill="none", marker_end="url(#arrowhead)")
    animate = ET.SubElement(path, "animate", attributeName="d", from_=f"M{i*20} 200 Q{i*20+50} 100 {i*20+100} 200", to=f"M{i*20} 200 Q{i*20+50} 300 {i*20+100} 200", begin="0s", dur="4s", repeatCount="indefinite")

# Create an XML tree
tree = ET.ElementTree(root)

# Save the SVG file
tree.write("dance_diagram.svg")

print("SVG diagram generated as 'dance_diagram.svg'.")
```

This code creates an SVG diagram with lines, arrows, and Bezier curves. After generating the SVG, you can use external video editing software or a Python library like `ffmpeg-python` to convert the SVG to a MOV file. Converting SVG to MOV directly in Python is complex and typically requires external tools or libraries for video rendering.

OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com

# The Edit 
I edited this code because run as is it is pretty boring - its a bunch of arcs that rotate around mirror symmetry. I added some random variables and made the screen size larger but still it is not super exciting. I do find it quiet and zen though - perhaps if we moved like these lines - which remind me of water through a peaceful water fall - we would have peace. Maybe not - maybe I should go something more direct actiony. 

my goal is to do this daily - so not every write up or every piece will be thorough or even good. But hopefully some will . 