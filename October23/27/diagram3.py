import matplotlib.pyplot as plt

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(10, 5))

# Textual Notation
# This notation uses text to convey the narrative and mood of the composition.
# It focuses on the lyrics and their emotional significance.

ax.text(0.5, 2.5, "O Viridissima Virgo", fontsize=14, ha='left', va='center', color='black')
ax.text(0.5, 2, "O most green virgin", fontsize=12, ha='left', va='center', color='black')
ax.text(0.5, 1.5, "You are the flower of the fields", fontsize=12, ha='left', va='center', color='black')
ax.text(0.5, 1, "In the meadows you shine", fontsize=12, ha='left', va='center', color='black')

# Title and composer
ax.text(3, 3.8, 'O Viridissima Virgo', fontsize=14, ha='center', va='center', color='black')
ax.text(3, 3.6, 'Hildegard von Bingen', fontsize=10, ha='center', va='center', color='black')

# Set axis limits and labels
ax.set_xlim(0, 6)
ax.set_ylim(0, 4.5)
ax.set_xlabel('Position')
ax.set_ylabel('Textual Notation')

# Display the notation
plt.grid(False)
plt.axis('off')
plt.show()
