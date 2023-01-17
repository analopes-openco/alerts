from abc import ABC, abstractclassmethod


class ISlack(ABC):
    @abstractclassmethod
    def send_message(self):
        raise NotImplementedError()
