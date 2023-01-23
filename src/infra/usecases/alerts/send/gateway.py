from dataclasses import dataclass
from typing import Optional, List
from abc import ABC, abstractclassmethod
from src.infra.slack.client import SlackClient
from src.infra.slack.message import SlackMessage


@dataclass
class Link:
    name: str
    url: str


@dataclass
class Body:
    text: str
    link: Optional[Link]


class IAlertsSendMessage(ABC):
    def create_simple_message(self, body: str) -> dict:
        raise NotImplementedError()

    def create_block_message(
        self, title: str, body: List[Body], subtitle: list = None
    ) -> dict:
        raise NotImplementedError()


class AlertsSendMessageImpl:
    def __init__(self):
        self.slack_message = SlackMessage()

    def create_simple_message(self, text: str) -> dict:
        """Return a message with simple text.

        Keyword arguments:
        text -- message text in string format
        """
        return self.slack_message.simple_text(text=text)

    def create_block_message(
        self, title: str, body: List[Body], subtitle: list = None
    ) -> dict:
        """Return a message with elements block.

        Keyword arguments:
        title -- message title in string format
        body -- list section of body
        subtitle -- text in markdown format
        """

        components = [
            self.slack_message.block_header(title=title),
            self.slack_message.divider(),
        ]

        if subtitle:
            components.insert(1, self.slack_message.block_context(texts=subtitle))

        for element in body:
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

        return self.slack_message.blocks(components)

    def send_message(self, url_file, report):
        return SlackClient().send_message__via_webhook(
            data=self.create_message(text=report, url=url_file)
        )
