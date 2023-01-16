from pytest import fixture
from settings import Settings
from src.slackapi import SlackAPI


@fixture
def url():
    return Settings.WEBHOOK_SLACK


@fixture
def channel():
    return Settings.SLACK_CHANNEL_TEST


def test_webhook_send_message_successfully(requests_mock, url, channel):
    requests_mock.post(url=f"{url}/{channel}", status_code=200, text="ok")

    slack_api = SlackAPI()
    response = slack_api.webhook(data={"text": "Hello, World!"})
    assert response.text == "ok"
    assert response.status_code == 200
