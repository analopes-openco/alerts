from enum import Enum
from typing import Type


class StyleButton(Enum):
    BLACK = None
    GREEN = "primary"
    RED = "danger"


class Message:
    def blocks(self, components: list) -> dict:
        """Return a message.

        Keyword arguments:
        components -- series of components to create messages
        """
        return {"blocks": components}

    def divider(self):
        """Return a content divider."""
        return {"type": "divider"}

    def header(self, title: str) -> dict:
        """Return a plain text displayed in a larger, bold font.

        Keyword arguments:
        title -- message title in string format
        """

        return {"type": "header", "text": {"type": "plain_text", "text": title}}

    def context(self, texts: list) -> dict:
        """Returns the message context.

        Keyword arguments:
        texts -- context texts in markdown format
        """

        elements = []
        for text in texts:
            elements.append({"text": text, "type": "mrkdwn"})

        return {"type": "context", "elements": elements}

    def section(self, text: str, accessory: dict = None) -> dict:
        """Return a flexible blocks used as a plain text block, in combination with any of the block elements.

        Keyword arguments:
        text -- section text in markdown format
        accessory -- any of the block elements
        """

        block = {"type": "section", "text": {"type": "mrkdwn", "text": text}}

        if accessory:
            block.update({"accessory": accessory})

        return block

    def button(
        self, name: str, url: str, style: Type[StyleButton] = StyleButton.BLACK.value
    ) -> dict:
        """Return a button.

        Keyword arguments:
        name -- defines the text of the button
        url -- browser link
        style -- decorates buttons with color schemes
        """

        block = {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": name,
            },
            "url": url,
        }

        if style:
            block.update({"style": style})

        return block
