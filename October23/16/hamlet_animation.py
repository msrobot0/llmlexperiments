import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a sample network graph for Act 1
G_act1 = nx.Graph()
G_act1.add_edge("Hamlet", "Ophelia")
G_act1.add_edge("Hamlet", "Gertrude")

# Create a sample network graph for Act 2
G_act2 = nx.Graph()
G_act2.add_edge("Hamlet", "Ophelia")
G_act2.add_edge("Hamlet", "Gertrude")
G_act2.add_edge("Hamlet", "Polonius")

# Create a sample network graph for Act 3
G_act3 = nx.Graph()
G_act3.add_edge("Hamlet", "Ophelia")
G_act3.add_edge("Hamlet", "Gertrude")
G_act3.add_edge("Hamlet", "Polonius")
G_act3.add_edge("Laertes", "Ophelia")

# Create a list of network graphs for each act
acts = [G_act1, G_act2, G_act3]

# Create a function to update the plot for each act
def update_plot(frame):
    plt.clf()
    G = acts[frame]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1000, font_size=10, font_color="black")
    plt.title(f"Act {frame+1}")
    plt.axis('off')

# Create an animation and set repeat=True
ani = FuncAnimation(plt.gcf(), update_plot, frames=len(acts), repeat=True, interval=2000)  # Adjust interval as needed

# Display the animation
plt.show()
