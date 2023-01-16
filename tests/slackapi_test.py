import json
from pytest import fixture
from http import HTTPStatus
from settings import Settings
from src.slackapi import SlackAPI


@fixture
def url():
    hooks_slack = Settings.WEBHOOK_SLACK
    channel = Settings.SLACK_CHANNEL_TEST
    return f"{hooks_slack}/{channel}"


@fixture
def data():
    return {"text": "Hello, World!"}


def test_webhook_send_message_successfully(requests_mock, url, data):
    requests_mock.post(url=url, status_code=200, text="ok")
    send_message = SlackAPI().webhook(data=data)
    assert send_message.request.method == "POST"
    assert send_message.request.url == url
    assert send_message.request.data == json.dumps({"text": "Hello, World!"})
    assert send_message.status_code == HTTPStatus.OK
    assert send_message.response == "ok"
    assert isinstance(send_message.response, str)


def test_webhook_send_message_error(requests_mock, url, data):
    requests_mock.post(url=url, status_code=400, text="invalid_payload")
    send_message = SlackAPI().webhook(data=data)
    assert send_message.request.method == "POST"
    assert send_message.request.url == url
    assert send_message.request.data == json.dumps({"text": "Hello, World!"})
    assert send_message.status_code == HTTPStatus.BAD_REQUEST
    assert send_message.response == "invalid_payload"
    assert isinstance(send_message.response, str)
