# Experiment 3: Poem

![[poem.png]]
[View the Code and Output on GitHub](https://github.com/msrobot0/llmlexperiments/blob/main/README.md)
I thought today would be quick. I was working on writing prompts to autogenerate music with csound but I was having lots of problems - in a large part because my csound knowledge is poor.  This morning I met with a poetry reading/writing group that I have been meeting with on and off since before the pandemic! It felt so damn good. And I thought- -I am going to write python to write poetry.

I listened to [John Giorno](https://www.youtube.com/watch?v=U18MJLVrxUU) last night reading "thanx for nothing."  I also watched [this recording of thanx for nothing](https://www.youtube.com/watch?v=-tO_r7U_MLo). As I write this maybe I should have written a prompt that looked at both these poems or inspiration but I did not.  What this did do was inspire me to output a spoken word piece - which is text to speech and sounds like crap - but hey LLMS did it. 

## here is the process

### prompt
> write a text to speech poem in python based on nlk concordances as the prompts written today

I wrote a bunch of prompts about music to end violence. 
This is the chat response: 

### LLM 
Creating a text-to-speech poem in Python based on NLTK concordances can be an interesting creative exercise. Below is an example of a Python code that generates a poem using NLTK concordance lines and then converts it to speech using the `gTTS` (Google Text-to-Speech) library. To run this code, you'll need to install NLTK and gTTS if you haven't already:

```bash
pip install nltk
pip install gTTS
```

Now, you can create a Python script (e.g., `poem_generator.py`) with the following code:

```python
import nltk
from nltk.corpus import reuters
from nltk.text import Text
from nltk.tokenize import sent_tokenize
from gtts import gTTS
import os

# Download the Reuters corpus if not already downloaded
nltk.download("reuters")

# Load the Reuters corpus
reuters_corpus = Text(reuters.words())

# Define a target word for concordances
target_word = "freedom"

# Generate concordances for the target word
concordances = reuters_corpus.concordance_list(target_word, width=100, lines=10)

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
```

In this code:

- We use NLTK to load the Reuters corpus and generate concordances for a target word, which is set to "freedom" in this example.

- We extract sentences containing the target word and create a poem from these sentences.

- The poem is saved to a text file and then converted to speech using the `gTTS` library.

- Finally, the generated poem is played as an MP3 audio file.

You can replace the target word and adapt the code to generate poems based on different prompts or words of your choice.
OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com

Then I thought oh I am going to ask the llm to convert the text to speech (not so great) - there is an opportunity for improvement he

## Reflections
This did not work out of the box - because the reuters feed is no longer available. When I told the LLM this, it was replaced with shakespeare's hamlet, and the target word was replaced with to. 


I included this output as poem.py, poem.txt, and poem.mp3. 

All the generated art so for feels really random, and in the animation the random library is used, rather that something that will generate a pattern like sine, or cosine. I would like to explore this in the future.  But when I heard this output at first, I was not sure whether or not this was actually different from the actual Shakespeare text. This is a fail.  so I figured lets give it some poetic structure - a villanelle. 

## prompt 2
> make the poem a villanelle

The output to this was to autogenerate words and turn it into a villanelle. It had nothing to do with the previous output. I gave it a thumbs down and was offered a solution that took the previous solution with hamlet and put it into vilanelle form. 
### the output
A villanelle is a 19-line poem with a specific structure and rhyme scheme (AABAABAA, AABAABAA, AABAA), and it often explores a theme or repeats a refrain throughout the poem. Here's a Python script that generates a villanelle-style poem based on NLTK concordances from a chosen text source:

```python
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
```

In this code:

- We've adapted the generated sentences to follow a villanelle-style structure (AABAABAA, AABAABAA, AABAA).

- The reordered lines are saved to a text file, and the poem is then converted to speech.

This code will generate a villanelle-style poem using sentences from "Hamlet" that contain the target word "to." You can adjust the target word or the text source to create different villanelles based on your preferences.
OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com

This was a bit better: 
The full poem is here

But the audio and the poem and code is available under villanelle_poem.txt.mp3 villanelle_poem.txt villanelle_poem.py

>tion come , He may approue our eyes , and speake to it Hor . Tush , tush , ' twill not appeare Bar .
are them . Stand : who ' s there ? Hor . Friends to this ground Mar . And Leige - men to the Dane Fr
tion come , He may approue our eyes , and speake to it Hor . Tush , tush , ' twill not appeare Bar .
are them . Stand : who ' s there ? Hor . Friends to this ground Mar . And Leige - men to the Dane Fr
tion come , He may approue our eyes , and speake to it Hor . Tush , tush , ' twill not appeare Bar .
are them . Stand : who ' s there ? Hor . Friends to this ground Mar . And Leige - men to the Dane Fr
tion come , He may approue our eyes , and speake to it Hor . Tush , tush , ' twill not appeare Bar .
that ' s dead Mar . Thou art a Scholler ; speake to it Horatio Barn . Lookes it not like the King ? 

It also really makes no sense, not sure if it even makes audio sense  also I thought villanelles ended with couplets. 

The Experiment continues. 