import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(10, 5))

# Abstract and symbolic elements
# These elements are highly abstract and inspired by Hildegard von Bingen's mystical notations

# Symbolic shapes and lines
ax.add_patch(patches.Ellipse((2, 3), width=1, height=0.5, fill=False, edgecolor='black', linewidth=2))
ax.plot([1, 3], [2, 2.5], 'k-', linewidth=2)

# Abstract shapes with symbols
ax.add_patch(patches.Polygon([[4, 1], [4.5, 2], [5, 1]], closed=True, fill=False, edgecolor='red', linewidth=2))
ax.text(4.75, 1.5, '✧', fontsize=12, color='green', ha='center')

# Unconventional labels and symbols
ax.annotate('❁', (3.75, 2), (3.75, 2.5), fontsize=16, color='blue', ha='center')
ax.annotate('✹', (2, 2.5), (2, 3), fontsize=16, color='purple', ha='center')

# Title and composer
ax.text(3, 4, 'O Viridissima Virga', fontsize=14, ha='center', va='center')
ax.text(3, 3.8, 'Hildegard von Bingen', fontsize=10, ha='center', va='center')

# Set axis limits and labels
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 4.5)
ax.set_xlabel('Time')
ax.set_ylabel('Interpretation')

# Display the diagram
plt.grid(False)
plt.axis('off')
plt.show()


