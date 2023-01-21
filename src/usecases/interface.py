from abc import ABC, abstractclassmethod


class IReportAlert(ABC):
    @abstractclassmethod
    def create_message(self):
        raise NotImplementedError()

    @abstractclassmethod
    def send_message(self):
        raise NotImplementedError()
