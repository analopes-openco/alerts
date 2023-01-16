import json
import requests
from settings import Settings
from typing import Type, Dict


class SlackAPI:
    def __init__(self) -> None:
        self.url = Settings.WEBHOOK_SLACK
        self.header = {"Content-type": "application/json"}

    def webhook(self, data: Dict) -> str:
        channel = Settings.SLACK_CHANNEL_TEST
        response = requests.post(
            url=f"{self.url}/{channel}", data=json.dumps(data), headers=self.header
        )
        return response
