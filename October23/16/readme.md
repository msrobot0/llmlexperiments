		![[hamlet_diagram.png]]
	I was talking with my friend Nicolas about LLMs and he said something about generating the diagrams of the relationships between the characters in hamlet.  

I am sort of interested in seeing the interactions between all the characters in hamlet as a a dance - how often to characters talk to each other in which scenes and how does this change over time, where do the scenes take place etc. 

I was also interested to see if Chat GPT could create a prompt that could create a script - TLDR - I was unsuccesful. I was also unsuccesful in createing anything more specific. Perhaps I need to work on my prompts. I am also a bit tired. 

## Prompt
> create a python script that shows how the characters in hamlet interact with each other overtime make an animated network diagram and animate the diagram so that we see how the character relationships change in each scene


## Response
Creating an animated network diagram of how the characters in "Hamlet" interact with each other over time is a complex task that requires a combination of text processing, data visualization, and animation libraries. Here's a high-level outline of how you might approach this task:

1. **Data Preparation**:
   - First, you need to extract the data from the play. You can use a digital text of "Hamlet" and write a Python script to parse the text to identify which characters are in each scene together. You will also need to note the emotional connections between characters.

2. **Data Representation**:
   - Create a data structure to represent the relationships between characters in each scene. You might use a graph or network structure where characters are nodes, and interactions are edges.

3. **Data Visualization**:
   - Utilize a data visualization library like NetworkX and Matplotlib to create static network diagrams for each scene. You can assign different colors or styles to edges to represent the nature of interactions (e.g., positive, negative, neutral).

4. **Animation**:
   - For animation, you can use a library like NetworkX or Plotly to create animated network diagrams. You will need to update the network structure for each scene and save it as a sequence of images or a video.

Here's a simplified example of how you can create a static network diagram using NetworkX and Matplotlib:

```python
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
```

For the animation part, you can extend this by iterating through scenes and updating the graph structure for each scene. You can then use a library like matplotlib's `FuncAnimation` or Plotly to create an animated sequence.

Creating a complete animated network diagram with changing character relationships throughout the entire play is a substantial project that requires time and effort. You may also need to create a data structure to track how the character relationships change over time as the play progresses.

OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com

## Thoughts 
This worked pretty much out of the box but dd not animate. The graphic was sort of cool.  The relationships are not super nuanced, but it is something. 

i want to get more complex and nuanced interactions. I am thinking of training my own ML - or having my own graph db of word embeddings populated with my own documents.  Maybe I should have chat use c++ or haskell or rust or something. 

### making it animate
I added this prompt
> come on - you can add an animation to show how this relationship changes between act 1 act2 and act 3

## result
Creating a complete animated network diagram with scene-by-scene changes in character relationships in a play as complex as "Hamlet" is a substantial project that goes beyond the scope of a single text-based response. However, I can provide you with a simplified example of how you might create an animation to show changes in character relationships between Act 1, Act 2, and Act 3 using NetworkX and Matplotlib.

Here's a basic Python script to create a simple animated network diagram:

```python
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

# Create an animation
ani = FuncAnimation(plt.gcf(), update_plot, frames=len(acts), repeat=False)

# Display the animation
plt.show()
```

This code sets up a basic animation that displays the network diagram for each act (Act 1, Act 2, and Act 3) with changing character relationships. You can extend this approach by adding more acts and more complex relationships as needed.

Please note that this is a simplified example. In a real-world project, you would need to parse the play's text to extract character interactions for each scene, which is a non-trivial task.

OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com

### Upgrades
Changing repeat to True makes this loop. I do think this is an interesting pedogogical tool for learning code - not so much for understanding Hamlet. 


