# Generating a Flask Web App
Today I generated a web app using a few lines of chat gpt prompts.  I dont think it would run on a server since it writes to the local file system and so has some permission / security flaws - but it is still pretty darn cool!

First I had LLM generate a program that calculated an astrological chart.. Then had it generate a visualization of the chart, which was not that great, then I had LLM generate music. I asked that the note and the tempo be linked to the zodiac and house of the different planets - I am not sure this happened with any sort of finesse but it happened. 

I then asked the LLM to allow the user to input birthdata, and finally I asked the LLM to create a flask web app and a webpage that accepted the birth data and this is the app you see. 

There were a bunch of things that did not work out of the box, modules were not imported, as I said this has major security issues, and it looks pretty bad - but for a few lines of prompt and something that was generated in about 10 minutes this is pretty amazing.

