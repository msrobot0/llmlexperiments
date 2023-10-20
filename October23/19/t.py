import networkx as nx
import matplotlib.pyplot as plt

def color_graph(G):
    # Create a dictionary to store colors assigned to nodes
    color_map = {}

    # List of available colors
    available_colors = list(range(1, len(G) + 1))

    # Traverse each node in the graph
    for node in G.nodes():
        # Get adjacent node colors
        neighbor_colors = {color_map.get(neighbor, 0) for neighbor in G.neighbors(node)}

        # Find the first available color
        for color in available_colors:
            if color not in neighbor_colors:
                color_map[node] = color
                break
        if node not in color_map:
            color_map[node] = 0

    return [color_map[node] for node in G.nodes()]

def draw_graph(G, colors):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=colors, cmap=plt.cm.rainbow, node_size=500, font_size=10)
    plt.show()

# Create a sample graph (you can modify this part for your specific graph)
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (4, 5), (5, 1)])

# Color the graph
colors = color_graph(G)

# Draw the colored graph
draw_graph(G, colors)

# Check if the graph is properly colored (no adjacent nodes have the same color)
is_colorable = all(colors[u] != colors[v] for u, v in G.edges())
if is_colorable:
    print("The graph is properly colored.")
else:
    print("The graph is not properly colored.")

