from datetime import datetime, timedelta
from src.domain.entities.slack_message import Message, Body, Link
from src.infra.usecases.slack.send.gateway import SlackAlertImpl


class Alert:
    def __init__(self):
        self.slack_alert = SlackAlertImpl()

    def report_geru(self):
        body = Body(
            text="*GERU*\nFIDC-1: 150\nFIDC-2: 150\nLECCA: 150\nRUGE: 150",
            link=Link(name="See records", url="https://google.com"),
        )
        return body

    def report_rebel(self):
        body = Body(
            text="*REBEL*\nFIDC-1: 150\nFIDC-2: 150\nLECCA: 150\nRUGE: 150",
            link=Link(name="See records", url="https://google.com"),
        )
        return body

    def send_message(self):
        return self.slack_alert.send_structured_message(
            message=Message(
                title="Rastreamento",
                subtitle=[
                    f"<!channel> *{(datetime.now() - timedelta(1)).strftime('%d-%m-%Y')}*"
                ],
                body=[self.report_geru(), self.report_rebel()],
            )
        )

        return self.slack_alert.send_simple_message(message="Hello World!")
