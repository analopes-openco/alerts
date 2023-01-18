import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
    DB_CONNECTION_URL = os.getenv("DB_CONNECTION_URL")
