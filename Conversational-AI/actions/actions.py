# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser

class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"
    
    async def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        video_url="https://www.youtube.com/watch?v=du4DDUcC2gw"
        dispatcher.utter_message("wait... Playing the video.")
        webbrowser.open(video_url)
        return []

class ActionPrecautions(Action):
    def name(self) -> Text:
        return "action_precautions"
    
    async def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        url="https://kidshealth.org/en/parents/coronavirus-stop-spread.html"
        dispatcher.utter_message("wait... Redirecting.")
        webbrowser.open(url)
        return []



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
