import nltk
from nltk.corpus import gutenberg
from nltk.text import Text
from gtts import gTTS
import os

# Download the Gutenberg corpus if not already downloaded
nltk.download("gutenberg")

# Load the Gutenberg corpus (in this case, we're using "Hamlet" by William Shakespeare)
hamlet_corpus = Text(gutenberg.words("shakespeare-hamlet.txt"))

# Define a target word for concordances
target_word = "to"

# Generate concordances for the target word
concordances = hamlet_corpus.concordance_list(target_word, width=100, lines=10)

# Extract sentences containing the target word
sentences = set()
for conc in concordances:
    sentences.add(conc.line)

# Create a villanelle-style poem
poem_lines = list(sentences)
villanelle_poem = []

# Reorder the poem lines to match the villanelle structure (AABAABAA, AABAABAA, AABAA)
for i in range(7):
    villanelle_poem.append(poem_lines[i % 2])

villanelle_poem.append(poem_lines[6])  # The final AABAA stanza

# Save the poem to a text file
with open("villanelle_poem.txt", "w") as poem_file:
    poem_file.write("\n".join(villanelle_poem))

# Convert the poem to speech
poem_text = ""
with open("villanelle_poem.txt", "r") as poem_file:
    poem_text = poem_file.read()

tts = gTTS(poem_text, lang="en")
tts.save("villanelle_poem.mp3")

# Play the generated villanelle-style poem
os.system("mpg123 villanelle_poem.mp3")

