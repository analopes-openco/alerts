from pytest import fixture
from src.domain.entities.slack_message import Message, Body, Link
from src.infra.usecases.slack.send.gateway import SlackAlertImpl


@fixture
def slack():
    return SlackAlertImpl()


def test_send_simple_message_success(mocker, slack):
    mocker.patch.object(SlackAlertImpl, "send_simple_message", return_value="Slack: ok")
    send_message = slack.send_simple_message(message="Hello, World!")
    assert send_message == "Slack: ok"


def test_send_simple_message_error(mocker, slack):
    mocker.patch.object(
        SlackAlertImpl,
        "send_simple_message",
        return_value="SlackError: Bad Request - no_text",
    )
    send_message = slack.send_simple_message(message={})
    assert send_message == "SlackError: Bad Request - no_text"


def test_send_structured_message_success(mocker, slack):
    mocker.patch.object(
        SlackAlertImpl, "send_structured_message", return_value="Slack: ok"
    )

    send_message = slack.send_structured_message(
        message=Message(
            title="Title",
            subtitle=["subtitulo_1", "subtitulo_2"],
            body=[
                Body(
                    text="1 - body text",
                    link=Link(name="Click me", url="https://google.com"),
                ),
                Body(
                    text="2 - body text",
                    link=Link(name="Click me", url="https://google.com"),
                ),
            ],
        )
    )
    assert send_message == "Slack: ok"


def test_send_structured_message_error(mocker, slack):
    mocker.patch.object(
        SlackAlertImpl,
        "send_structured_message",
        return_value="SlackError: Bad Request - invalid_blocks",
    )

    send_message = slack.send_structured_message(
        message=Message(title="", subtitle=[], body=[])
    )
    assert send_message == "SlackError: Bad Request - invalid_blocks"
