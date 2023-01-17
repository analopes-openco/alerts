class SlackException(Exception):
    def __init__(self, message: str):
        super(SlackException, self).__init__(message)
        self.error = "Unknown"


class SlackBadRequestException(SlackException):
    def __init__(self, error: str, message: str):
        super(SlackBadRequestException, self).__init__(message)
        self.error = error
