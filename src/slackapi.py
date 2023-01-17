import json
import requests
from typing import Type
from settings import Settings
from collections import namedtuple
from requests import Request, Response


class SlackAPI:
    def __init__(self) -> None:
        self._url = Settings.SLACK_WEBHOOK_URL
        self._header = {"Content-type": "application/json"}
        self._default_return = namedtuple("SlackAPI", "status_code request response")

    def __send_http_request(self, req_prepared: Type[Request]) -> Type[Response]:
        session = requests.Session()
        return session.send(req_prepared)

    def webhook(self, data: dict) -> any:
        req = Request(
            method="POST",
            url=self._url,
            data=json.dumps(data),
            headers=self._header,
        )
        response = self.__send_http_request(req_prepared=req.prepare())

        if 400 <= response.status_code < 500:
            raise SlackBadRequestException(, response.text)

        elif response.status_code >= 500:
            raise SlackException(message)

        else:
            return self._default_return(
                status_code=response.status_code, request=req, response=response.text
            )