import json
from pytest import fixture
from http import HTTPStatus
from http import HTTPMethod
from settings import Settings
from src.slackapi import SlackAPI


@fixture
def url(settings):
    return Settings.SLACK_WEBHOOK_URL


@fixture
def data():
    return {"text": "Hello, World!"}


def test_webhook_send_message_success(requests_mock, url, data):
    requests_mock.post(url=url, status_code=200, text="ok")
    send_message = SlackAPI().webhook(data=data)

    # test request
    assert send_message.request.url != ""
    assert send_message.request.url == url
    assert send_message.request.method == HTTPMethod.POST
    assert send_message.request.data == json.dumps(data)

    # test response
    assert send_message.status_code == HTTPStatus.OK
    assert send_message.response == "ok"
    assert isinstance(send_message.response, str)


def test_webhook_send_message_error(requests_mock, url, data):
    requests_mock.post(url=url, status_code=400, text="invalid_payload")
    send_message = SlackAPI().webhook(data=data)

    # test request
    assert send_message.request.url != ""
    assert send_message.request.url == url
    assert send_message.request.method == HTTPMethod.POST
    assert send_message.request.data == json.dumps(data)

    # test response
    assert send_message.status_code == HTTPStatus.BAD_REQUEST
    assert send_message.response == "invalid_payload"
    assert isinstance(send_message.response, str)
