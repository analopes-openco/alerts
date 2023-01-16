from src.slackapi import SlackAPI
from src.interface import ISlack


class TrackingAlert(ISlack):
    def send_message(self):
        data = {}
        return SlackAPI().webhook(data=data)


alert = TrackingAlert().send_message()
print(alert.text)
