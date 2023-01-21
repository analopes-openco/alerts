from src.usecases.interface import IReportAlert
from src.infra.slack.client import SlackClient
from src.infra.slack.message import Message, StyleButton


class ReportAlert(IReportAlert):
    def create_message(self):
        message = Message()

        components = [
            message.header(title="Rastreamento"),
            message.context(texts=["*17 Janeiro 2023*"]),
            message.divider(),
            message.section(
                text=":alert: |  *FIDC-1*  | :alert:",
                accessory=message.button(
                    name="See records",
                    url="https://google.com",
                    style=StyleButton.RED.value,
                ),
            ),
            message.section(text="*REBEL*: 150 registros\n*GERU*: 150 registros"),
            message.divider(),
            message.section(
                text=":alert: |  *FIDC-2*  | :alert:",
                accessory=message.button(
                    name="See records",
                    url="https://google.com",
                    style=StyleButton.RED.value,
                ),
            ),
            message.section(text="*REBEL*: 150 registros\n*GERU*: 150 registros"),
            message.divider(),
        ]
        return message.blocks(components)

    def send_message(self):
        message = self.create_message()
        print(message)
        # return SlackClient().webhook(data=message)
