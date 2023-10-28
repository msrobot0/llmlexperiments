from pyvis.network import Network

# Create a Network instance
G = Network(notebook=False)
#G.barnes_hut()


# Create a Network instance
G = Network(notebook=False)

# Add nodes
G.add_node("Tryptophan", label="Tryptophan", title="Amino Acid")
G.add_node("Methyltransferase", label="Methyltransferase", title="Enzyme")
G.add_node("Methylated Tryptophan", label="Methylated Tryptophan", title="Methylated Amino Acid")

# Add edges
G.add_edge("Tryptophan", "Methyltransferase", title="Methylation")
G.add_edge("Methyltransferase", "Methylated Tryptophan", title="Methylation")

# Save the graph to an HTML file
G.write_html("methylation_interactive.html")