import xml.etree.ElementTree as ET
import random
# Create SVG root element
root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", width="1000", height="1000")

# Create definitions for the arrowhead marker
defs = ET.SubElement(root, "defs")
marker = ET.SubElement(defs, "marker", id="arrowhead", markerWidth="10", markerHeight="7", refX="0", refY="3.5", orient="auto")
polygon = ET.SubElement(marker, "polygon", points="0 0, 10 3.5, 0 7", fill="gray")

# Create paths with arrows and Bezier curves
for i in range(50):
    path = ET.SubElement(root, "path", d=f"M{20*random.randint(-10,10)} 0 Q{20+50*random.randint(-10,10)} 0 {i*20+100} 0", stroke="gray", stroke_width="{{random.randint(0,4)}}", fill="none", marker_end="url(#arrowhead)")
    animate = ET.SubElement(path, "animate", attributeName="d", from_=f"M{i*20*random.randint(-10,10)} 200 Q{i*20+50*random.randint(-10,10)} 100 {i*20+100*random.randint(-10,10)} 200", to=f"M{random.randint(-10,10)} 1000 Q{random.randint(-10,10)*20+50} 300 {i*20+100*random.randint(-10,10)} 200", begin="0s", dur="5s", repeatCount="indefinite")

# Create an XML tree
tree = ET.ElementTree(root)

# Save the SVG file
tree.write("dance_diagram.svg")

print("SVG diagram generated as 'dance_diagram.svg'.")