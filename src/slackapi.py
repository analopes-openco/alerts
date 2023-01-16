import json
from settings import Settings
from typing import Type, Dict
from requests import requests, Request


class SlackAPI:
    def __init__(self) -> None:
        self.url_prefix = Settings.WEBHOOK_SLACK
        self.header = {"Content-type": "application/json"}

    def webhook(self, data: Dict) -> Type[Request]:
        url_sufix = Settings.SLACK_CHANNEL_TEST
        req = requests.post(
            url=f"{self.prefix}/{url_sufix}", data=json.dumps(data), headers=self.header
        )

        return req.json()
