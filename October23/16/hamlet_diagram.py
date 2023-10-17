import networkx as nx
import matplotlib.pyplot as plt

# Create a sample network graph
G = nx.Graph()
G.add_edge("Hamlet", "Ophelia")
G.add_edge("Hamlet", "Gertrude")
G.add_edge("Hamlet", "Claudius")
G.add_edge("Ophelia", "Polonius")
G.add_edge("Laertes", "Ophelia")
G.add_edge("Polonius", "Ophelia")
G.add_edge("Polonius", "Hamlet")
G.add_edge("Rosencrantz", "Hamlet")
G.add_edge("Guildenstern", "Hamlet")
G.add_edge("Horatio", "Hamlet")

# Plot the network graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1000, font_size=10, font_color="black")
edge_labels = {("Hamlet", "Ophelia"): "Love", ("Hamlet", "Gertrude"): "Mother-Son", ("Hamlet", "Claudius"): "Conflict", ("Polonius", "Hamlet"): "Conflict"}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

plt.title("Character Interactions in 'Hamlet'")
plt.axis('off')
plt.show()
