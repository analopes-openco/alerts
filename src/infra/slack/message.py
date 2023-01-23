# https://api.slack.com/reference/surfaces/formatting
from enum import Enum


class StyleButton(Enum):
    BLACK = None
    GREEN = "primary"
    RED = "danger"


class SlackMessage:
    def simple_text(self, text: str) -> dict:
        """Return a plain text block.

        Keyword arguments:
        text -- message text in string format
        """
        return {"text": text}

    def blocks(self, components: list) -> dict:
        """Return a message.

        Keyword arguments:
        components -- series of components to create messages
        """
        return {"blocks": components}

    def block_header(self, title: str) -> dict:
        """Return a plain text displayed in a larger, bold font.

        Keyword arguments:
        title -- message title in string format
        """

        return {"type": "header", "text": {"type": "plain_text", "text": title}}

    def block_context(self, texts: list) -> dict:
        """Returns the message context.

        Keyword arguments:
        texts -- context texts in markdown format
        """

        elements = []
        for text in texts:
            elements.append({"text": text, "type": "mrkdwn"})

        return {"type": "context", "elements": elements}

    def block_section(self, text: str, accessory: dict = None) -> dict:
        """Return a flexible blocks used as a plain text block,
        in combination with any of the block elements.

        Keyword arguments:
        text -- section text in markdown format
        accessory -- any of the block elements
        """

        block = {"type": "section", "text": {"type": "mrkdwn", "text": text}}

        if accessory:
            block.update({"accessory": accessory})

        return block

    def block_actions(self, elements: list) -> dict:
        """Returns the message actions.

        Keyword arguments:
        elements -- any of the block elements
        """

        return {"type": "actions", "elements": elements}

    def element_button(self, name: str, url: str) -> dict:
        """Return a button.

        Keyword arguments:
        name -- defines the text of the button
        url -- browser link
        """

        return {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": name,
            },
            "url": url,
        }

    def divider(self):
        """Return a content divider."""
        return {"type": "divider"}
