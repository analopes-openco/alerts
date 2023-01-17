import os


class Settings:
    SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')
    DB_CONNECTION_URL = os.getenv('DB_CONNECTION_URL')
