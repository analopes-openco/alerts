import json
from pytest import fixture
from http import HTTPStatus
from settings import Settings
from src.slackapi import SlackAPI
from src.exceptions import SlackRequestException


@fixture
def url():
    return Settings.SLACK_WEBHOOK_URL


@fixture
def data():
    return {"text": "Hello, World!"}


def test_request_webhook(requests_mock, url, data):
    requests_mock.post(url=url)
    send_message = SlackAPI().webhook(data=data)
    assert send_message.request.url != ""
    assert send_message.request.method == "POST"
    assert send_message.request.data == json.dumps(data)


def test_webhook_send_message_success(requests_mock, url, data):
    requests_mock.post(url=url, status_code=200, text="ok")
    send_message = SlackAPI().webhook(data=data)
    assert send_message.status_code == HTTPStatus.OK
    assert send_message.response == "ok"


def test_webhook_send_message_error(requests_mock, url):
    requests_mock.post(url=url, status_code=400, text="invalid_payload")
    try:
        SlackAPI().webhook(data={})
    except SlackRequestException as e:
        assert e.status_code == HTTPStatus.BAD_REQUEST
        assert e.message == "invalid_payload"
