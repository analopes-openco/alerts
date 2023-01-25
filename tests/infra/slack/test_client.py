import json
from http import HTTPStatus
from settings import Settings
from pytest import fixture, raises
from src.infra.slack.client import SlackClient
from src.infra.slack.exceptions import SlackRequestException


@fixture
def url():
    return Settings.SLACK_WEBHOOK_URL


@fixture
def data():
    return {"text": "Hello, World!"}


@fixture
def client():
    return SlackClient()


def test_request_webhook(requests_mock, client, url, data):
    requests_mock.post(url=url)
    send_message = client.send_message_via_webhook(data=data)
    assert send_message.request.url != ""
    assert send_message.request.method == "POST"
    assert send_message.request.data == json.dumps(data)


def test_webhook_send_message_success(requests_mock, client, url, data):
    requests_mock.post(url=url, status_code=200, text="ok")
    send_message = client.send_message_via_webhook(data=data)
    assert send_message.status_code == HTTPStatus.OK
    assert send_message.response == "ok"


def test_webhook_send_message_error(requests_mock, client, url):
    requests_mock.post(url=url, status_code=400, text="invalid_payload")
    with raises(SlackRequestException) as e:
        client.send_message_via_webhook(data={})
    assert e.value.status_code == HTTPStatus.BAD_REQUEST
    assert e.value.message == "invalid_payload"
