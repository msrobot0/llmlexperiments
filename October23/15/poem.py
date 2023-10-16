import nltk
from nltk.corpus import gutenberg
from nltk.text import Text
from nltk.tokenize import sent_tokenize
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
    sentences.update(sent_tokenize(conc.line))

# Create a poem from the extracted sentences
poem = "\n".join(sentences)

# Save the poem to a text file
with open("poem.txt", "w") as poem_file:
    poem_file.write(poem)

# Convert the poem to speech
poem_text = ""
with open("poem.txt", "r") as poem_file:
    poem_text = poem_file.read()

tts = gTTS(poem_text, lang="en")
tts.save("poem.mp3")

# Play the generated poem
os.system("mpg123 poem.mp3")
