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
                symbol= symbols[alphabet.index(char) % len(symbols)]
                #symbol = symbols.pop(0) if symbols else '*'
                graphical_line += symbol

        graphical_poem.append(graphical_line)

    # Convert the graphical representation back to a string
    graphical_poem_str = '\n'.join(graphical_poem)

    return graphical_poem_str

# Example poem
poem = """
Thou shalt not judge
The size of your feet
The dog in the bed
The taste of the coffee
The noise in the room
The price of the ticket
The art on the wall
The maroon suit
The full sink
The lint in the machine
The oil in the stove
The oil in the pan
The oil on the rug
The smell of the pillow
The feel of the sheets
The sound of the alarm clock
The sound of the neighbors alarm clock
The strawberry alarm clock
That was a lot of work
"""

# Generate the graphical representation
graphical_representation = poem_to_graphical_representation(poem)

# Print the graphical representation
print(graphical_representation)
