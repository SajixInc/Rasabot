# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import Restarted, EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher

from main import Dose_Availability_District, Dose_Availability_Pincode, Dose_Availability_Lon_Lat, send_email

class ValidatepincodeForm(FormValidationAction):
    def name(self) -> Text:
        return "slot_pincode_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        required_slots = ["pincode", "date"]
        # "job_after_exit", "job_type", "acquire_skill", "skill_type", "any_business", "business_venture", "need_loan"

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        return [SlotSet("requested_slot", None)]

class ValidateDistrictForm(FormValidationAction):
    def name(self) -> Text:
        return "slot_district_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        required_slots = ["district_id", "date"]
        # "job_after_exit", "job_type", "acquire_skill", "skill_type", "any_business", "business_venture", "need_loan"

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        return [SlotSet("requested_slot", None)]

class ValidateLocationForm(FormValidationAction):
    def name(self) -> Text:
        return "slot_location_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        required_slots = ["lattitude", "longitude"]
        # "job_after_exit", "job_type", "acquire_skill", "skill_type", "any_business", "business_venture", "need_loan"

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        return [SlotSet("requested_slot", None)]

class ActionPincodeSubmit(Action):

    def name(self) -> Text:
        return "action_pincode_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message
        message=Dose_Availability_Pincode(tracker.get_slot('pincode'),tracker.get_slot('date'))
        dispatcher.utter_message(text=message)
        buttons = [
            {'payload': "/affirm", 'title': "Yes"},
            {'payload': "/deny", 'title': "No"},
        ]
        dispatcher.utter_message(text="Would you like to get the details on your email id?",buttons=buttons)

        return []

class ActionDistrictSubmit(Action):

    def name(self) -> Text:
        return "action_district_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message
        message=Dose_Availability_District(tracker.get_slot('district_id'),tracker.get_slot('date'))
        dispatcher.utter_message(text=message)
        buttons = [
            {'payload': "/affirm", 'title': "Yes"},
            {'payload': "/deny", 'title': "No"},
        ]
        dispatcher.utter_message(text="Would you like to get the details on your email id?",buttons=buttons)

        return []

class ActionLocationSubmit(Action):

    def name(self) -> Text:
        return "action_location_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message
        message=Dose_Availability_Lon_Lat(tracker.get_slot('lattitude'),tracker.get_slot('longitude'))
        dispatcher.utter_message(text=message)
        buttons=[
            {'payload':"/affirm",'title':"Yes"},
            {'payload':"/deny",'title':"No"},
        ]
        dispatcher.utter_message(text="Would you like to get the details on your email id?",buttons=buttons)
        return []

class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_send_mail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        send_email(tracker.get_slot("email"),message)
        dispatcher.utter_message(text="We have successfully sent the mail to your Email ID: {}".format(tracker.get_slot("email")))

        return []

class ActionRestart(Action):

    def name(self) -> Text:
      return "action_restart"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

      return [Restarted()]


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
