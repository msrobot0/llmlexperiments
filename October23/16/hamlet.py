import networkx as nx
import matplotlib.pyplot as plt

# Sample data for a single scene
scene_data = {
    "Characters": ["Hamlet", "Ophelia", "Claudius", "Polonius"],
    "Interactions": [("Hamlet", "Ophelia"), ("Hamlet", "Claudius"), ("Polonius", "Ophelia")],
    "Location": "Elsinore Castle"
}

# Create a network graph
G = nx.Graph()
for character in scene_data["Characters"]:
    G.add_node(character)
for interaction in scene_data["Interactions"]:
    G.add_edge(*interaction)

# Draw the network graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1000, font_size=10, font_color="black")
plt.title("Scene: Elsinore Castle")
plt.axis('off')
plt.show()

