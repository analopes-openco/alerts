import os


class Settings:
    WEBHOOK_SLACK = "https://hooks.slack.com/services"
    SLACK_CHANNEL_TEST = os.getenv('SLACK_CHANNEL_TEST')
    DB_CONNECTION = os.getenv('DB_CONNECTION')
