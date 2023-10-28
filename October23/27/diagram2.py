import matplotlib.pyplot as plt

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(10, 5))

# Extended Graphical Score Notation
# This notation includes symbols for repetition, dynamics, and a melodic contour.

# Define time and pitch data (simplified for illustration)
time = [1, 2, 3, 4, 5, 6, 7, 8]
pitch = [3, 4, 3, 2, 3, 1, 2, 3]

# Add markings for repetition (double bar line)
repeated_section = [2, 3, 4]
ax.plot(repeated_section, [3, 3, 3], marker='|', markersize=10, linestyle='--', color='black')

# Mark crescendo and decrescendo with arrows
ax.annotate('>', xy=(4, 3.5), fontsize=16, color='black')
ax.annotate('<', xy=(6, 2.5), fontsize=16, color='black')

# Title and composer
ax.text(4, 4.5, 'O Viridissima Virgo', fontsize=14, ha='center', va='center', color='black')
ax.text(4, 4.2, 'Hildegard von Bingen', fontsize=10, ha='center', va='center', color='black')

# Set axis limits and labels
ax.set_xlim(0.5, 8.5)
ax.set_ylim(0, 5)
ax.set_xlabel('Time')
ax.set_ylabel('Pitch')

# Display the notation
plt.grid(False)
plt.axis('off')
plt.show()
