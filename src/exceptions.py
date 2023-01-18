class SlackException(Exception):
    def __init__(self, message: str):
        super(SlackException, self).__init__(message)
        self.error = "Unknown"


class SlackRequestException(SlackException):
    def __init__(self, error: str, message: str, status_code: int):
        super(SlackRequestException, self).__init__(message)
        self.error = error
        self.message = message
        self.status_code = status_code
