import json
import requests
from typing import Type
from settings import Settings
from collections import namedtuple
from requests import Request, Response


class SlackAPI:
    def __init__(self) -> None:
        self.url = Settings.WEBHOOK_SLACK
        self.header = {"Content-type": "application/json"}
        self.default_return = namedtuple("SlackAPI", "status_code request response")

    def __send_http_request(self, req_prepared: Type[Request]) -> Type[Response]:
        session = requests.Session()
        return session.send(req_prepared)

    def webhook(self, data: dict) -> any:
        channel = Settings.SLACK_CHANNEL_TEST
        req = Request(
            method="POST",
            url=f"{self.url}/{channel}",
            data=json.dumps(data),
            headers=self.header,
        )
        response = self.__send_http_request(req_prepared=req.prepare())
        return self.default_return(
            status_code=response.status_code, request=req, response=response.text
        )
