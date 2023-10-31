


# actions.py
import openai  # Import the 'openai' module
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class GPT3Action(Action):
    def name(self):
        return "action_generate_response"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get("text")
        api_key = "KEY"  # Replace with your OpenAI API key

        # Set your OpenAI API key
        openai.api_key = api_key

        # Make a request to GPT-3
        response = openai.Completion.create(
            engine="davinci",  # Or specify another engine if needed
            prompt=user_message,
            max_tokens=50  # Adjust the token limit as needed
        )

        generated_response = response.choices[0].text

        # Send the generated response back to the chat
        dispatcher.utter_message(generated_response)

        return [SlotSet("generated_response", generated_response)]
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
