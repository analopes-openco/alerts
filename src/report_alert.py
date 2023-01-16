from api import SlackAPI
from interface import ISlack


class ReportAlert(ISlack):
    def send_message(self):
        data = {}
        return SlackAPI().webhook(data=data)


alert = ReportAlert().report()
print(alert.text)
