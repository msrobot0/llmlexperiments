def poem_to_graphical_representation(poem):
    # Split the poem into lines
    lines = poem.split('\n')

    # Define symbols and shapes
    symbols = ['*', '◆', '■', '▲', '▼', '○', '◎', '●', '◇']
    alphabet =list("abcdefghijiklmnopqrstuvwxyz")
    # Initialize the graphical representation
    graphical_poem = []

    # Iterate through each line of the poem
    for line in lines:
        graphical_line = ''

        # Assign symbols to characters in each line
        for char in line:
            if char == ' ':
                graphical_line += ' '  # Preserve spaces
            else:
                char = char.lower()
                try:
                    symbol= symbols[alphabet.index(char) % len(symbols)]
                except:
                    symbol = " "
                #symbol = symbols.pop(0) if symbols else '*'
                graphical_line += symbol

        graphical_poem.append(graphical_line)

    # Convert the graphical representation back to a string
    graphical_poem_str = '\n'.join(graphical_poem)

    return graphical_poem_str

# Example poem
poem = """
In the spirit of experimenting with random function generators this week I looked first the creative coding and math coding classes at superhi for inspiration.

But I did not look long because my new special interests — modular synths — inspired me.

Modular synthesizers are hardware boxes that generate electrical signals often to generate music (but I suppose could be used for other things) . I sort of like this article — but it is about a particular synth.
Try not to move here
everything is static

"""

# Generate the graphical representation
graphical_representation = poem_to_graphical_representation(poem)

# Print the graphical representation
print(graphical_representation)
