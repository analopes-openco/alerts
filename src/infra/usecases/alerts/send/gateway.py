from typing import Optional, List
from abc import ABC, abstractclassmethod
from src.infra.slack.client import SlackClient
from src.infra.slack.message import SlackMessage
from src.domain.entities.slack_message import Message, Body, Link
from src.infra.slack.exceptions import SlackException, SlackRequestException


class ISlackAlert(ABC):
    def send_simple_message(self, message: str) -> dict:
        raise NotImplementedError()

    def send_block_message(self, message: Message) -> dict:
        raise NotImplementedError()


class SlackAlertImpl(ISlackAlert):
    def __init__(self):
        self.slack_client = SlackClient()
        self.slack_message = SlackMessage()

    def __send_slack_client(self, data: dict) -> any:
        try:
            send = self.slack_client.send_message_via_webhook(data=data)
            return f"Slack: {send.response}"
        except SlackRequestException as e:
            return f"SlackError: {e.error} - {e.message}"
        except SlackException as e:
            return f"SlackError: {e.error} - {e.message}"

    def send_simple_message(self, message: str) -> dict:
        """Return a message with simple text.self.slack_message.si

        Keyword arguments:
        message -- message text in string format
        """

        return self.__send_slack_client(
            data=self.slack_message.simple_text(text=message)
        )

    def send_block_message(self, message: Message) -> dict:
        """Return a message with elements block.

        Keyword arguments:
        message:
            title -- message title in string format
            body -- list section of body
            subtitle -- text in markdown format
        """

        components = [
            self.slack_message.block_header(title=message.title),
            self.slack_message.divider(),
        ]

        if message.subtitle:
            components.insert(
                1, self.slack_message.block_context(texts=message.subtitle)
            )

        for element in message.body:
            if element.link:
                section = self.slack_message.block_section(
                    text=element.text,
                    accessory=self.slack_message.element_button(
                        name=element.link.name, url=element.link.url
                    ),
                )
            else:
                section = self.slack_message.block_section(text=element.text)

            components.append(section)
            components.append(self.slack_message.divider())

        return self.__send_slack_client(data=self.slack_message.blocks(components))
