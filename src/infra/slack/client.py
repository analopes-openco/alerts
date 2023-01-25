import json
import requests
from typing import Type
from settings import Settings
from collections import namedtuple
from requests import Request, Response
from src.infra.slack.exceptions import SlackException, SlackRequestException


class SlackClient:
    def __init__(self) -> None:
        self._url = Settings.SLACK_WEBHOOK_URL
        self._header = {"Content-type": "application/json"}
        self._default_return = namedtuple("SlackClient", "status_code request response")

    def __send_http_request(self, req_prepared: Type[Request]) -> Type[Response]:
        session = requests.Session()
        return session.send(req_prepared)

    def send_message_via_webhook(self, payload: dict) -> any:
        request = Request(
            method="POST",
            url=self._url,
            data=json.dumps(payload),
            headers=self._header,
        )
        response = self.__send_http_request(req_prepared=request.prepare())

        if 400 <= response.status_code < 500:
            raise SlackRequestException(
                error=response.reason,
                message=response.text,
                status_code=response.status_code,
            )

        elif response.status_code >= 500:
            raise SlackException(
                message=response.text, status_code=response.status_code
            )

        else:
            return self._default_return(
                status_code=response.status_code,
                request=request,
                response=response.text,
            )
