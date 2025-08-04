from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config/.env")


@dataclass
class TelegramConfig:
    TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID: int = int(os.getenv("TELEGRAM_CHAT_ID", 0))
    GROUP_ID: int = int(os.getenv("TELEGRAM_GROUP_ID", 0))
    CHANNEL_ID: int = int(os.getenv("TELEGRAM_CHANNEL_ID", 0))


@dataclass
class BybitConfig:
    API_KEY: str = os.getenv("BYBIT_API_KEY")
    API_SECRET: str = os.getenv("BYBIT_API_SECRET")
    REST_ENDPOINT: str = os.getenv("BYBIT_REST_ENDPOINT")
    WSS_ENDPOINT: str = os.getenv("BYBIT_WSS_ENDPOINT")


@dataclass
class LoggerConfig:
    LOG_LEVEL: str = os.getenv("LOG_LEVEL")
    LOG_FILE: str = os.getenv("LOG_FILE")


telegram = TelegramConfig()
bybit = BybitConfig()
logger = LoggerConfig()

__all__ = ["telegram", "bybit", "logger"]
