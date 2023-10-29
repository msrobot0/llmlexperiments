# Generate A Bot

The big thing people are talking about with AI is that we are going to have AI agents.  This will be a new programming and user interaction paradigm. Instead of people wandering around saerching for things or talking, agents trained on custom data sets will act like "people" with intention 
### acting without prompts

# My first bot 
prompt 
>create a python nlp chat bot for creating video game prompts

I am really interested in prompt engineering and in programs that create prompts that create programs or components. I tried to do that here - create a program to create prompts!

It was not super successful - but I feel like it could be a weird sort of poetry. 

![[img1 1.png]]

![[img2 1.png]]

![[img3 1.png]]

![[img4 1.png]]

## I asked for a nlp based on a decision tree
and I got this
![[img4a.png]]

I looked at the code- its chat3.py and it does not work much.

Surely you can do better I told the chat and then I got this rasa powered 
I was then introduced to the rasa language. Rasa is a Sanskrit word that means taste (or essence or aesthetic)

I was amazed to find this library! Fun! But I am not entirely sure how it works.  How does it work - and chat said...

>Rasa is an open-source framework for building conversational AI chatbots and virtual assistants. It is designed to handle natural language understanding, dialogue management, and language generation to create interactive and intelligent chatbots. Here's how Rasa works:

1. **Natural Language Understanding (NLU)**:
    
    Rasa begins by processing user inputs (text messages or speech) to understand the user's intent and extract relevant entities (pieces of information) using NLU models. Rasa NLU supports various NLP and machine learning libraries, including spaCy and scikit-learn, to perform tasks such as tokenization, part-of-speech tagging, and entity recognition.
    
2. **Domain and Intents**:
    
    In Rasa, you define a `domain.yml` file that specifies the intents (what users might say) and the responses (what the chatbot should say). You define intents for different user actions or requests (e.g., "greet," "book_flight," "get_weather"). This domain file also contains information about slots (user input that needs to be remembered) and actions (what the chatbot can do).
    
3. **Dialogue Management**:
    
    Rasa uses a dialogue management system to decide how the chatbot should respond to user inputs based on intents and entities. Dialogue management is often handled through stories, which define conversation flows. You create stories in a `stories.yml` file, specifying sequences of intents, entities, and chatbot responses to create interactive conversations.
    
4. **Machine Learning Models**:
    
    Rasa employs machine learning models to predict the next action in a conversation based on the dialogue management system and the current conversation state. The dialogue management can be rule-based, but it can also use reinforcement learning techniques.
    
5. **Custom Actions**:
    
    Rasa allows you to define custom actions that your chatbot can perform. These actions can include calling external APIs, looking up information in a database, or performing any other custom functionality. You can create custom actions in Python code and use them in your stories to enable more complex interactions.
    
6. **Training**:
    
    To make predictions and understand user inputs, Rasa needs training data. You provide training data in the form of labeled conversations (stories) and NLU data (examples of user messages with their corresponding intents and entities). Rasa trains machine learning models based on this data.
    
7. **Deployment**:
    
    Once your chatbot is trained and ready, you can deploy it on various platforms, including your website, messaging platforms like Slack or Facebook Messenger, or as a voice assistant.
    
8. **Integration**:
    
    You can integrate Rasa chatbots with various channels and services to make them accessible to users where they are, such as web chats, mobile apps, or voice interfaces. Rasa provides connectors and SDKs for such integrations.
    
9. **Continual Improvement**:
    
    Building a chatbot with Rasa is an iterative process. You can continually improve your chatbot by adding more training data, refining stories, and enhancing your NLU models.
    

Rasa's architecture and flexibility make it suitable for a wide range of conversational AI applications, from simple FAQ chatbots to complex virtual assistants. It offers a comprehensive set of tools to develop, train, deploy, and maintain chatbots that can engage in meaningful and interactive conversations with users.

OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com


![[img5.png]]

## rasa may have promise - but it does not work out of the box

I asked gpt for an ai integration and I did get something -but I have not tested it yet maybe I will test it tomorrow

I do have things I want to explore with chat
* twitch games
* prompt engineering 
* and nlp prompts + agents
* blender

It feels good to have a plan - a landscape. 

[the code](https://github.com/msrobot0/llmlexperiments/)
