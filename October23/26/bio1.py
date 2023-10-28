import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph to represent the methylation process
G = nx.DiGraph()

# Define nodes for the methylation steps
G.add_node("Tryptophan")
G.add_node("Methyltransferase")
G.add_node("Methylated Tryptophan")

# Define edges to represent the flow of the process
G.add_edge("Tryptophan", "Methyltransferase")
G.add_edge("Methyltransferase", "Methylated Tryptophan")

# Define labels for nodes
node_labels = {
    "Tryptophan": "Tryptophan",
    "Methyltransferase": "Methyltransferase",
    "Methylated Tryptophan": "Methylated Tryptophan",
}

# Draw the graph with labels
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10)
nx.draw_networkx_labels(G, pos, labels=node_labels)

# Display the diagram
plt.axis("off")
plt.show()

