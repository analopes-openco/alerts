from datetime import datetime, timedelta
from src.infra.usecases.alerts.send.gateway import AlertsSendMessageImpl


class Alert:
    def report_geru(self):
        return "*GERU*\nFIDC-1: 150\nFIDC-2: 150\nLECCA: 150\nRUGE: 150"

    def report_rebel(self):
        return "*REBEL*\nFIDC-1: 150\nFIDC-2: 150\nLECCA: 150\nRUGE: 150"

    def create_message(self):
        return Message().create_block_message(
            title="Rastreamento",
            body=[
                Body(
                    text=report_geru(),
                    link=Link(name="See records", url="https://google.com"),
                ),
                Body(
                    text=report_rebel(),
                    link=Link(name="See records", url="https://google.com"),
                ),
            ],
            subtitle=[f"<!channel> *{datetime.now() - timedelta(1)}*"],
        )
