from dataclasses import dataclass
from typing import Optional, Protocol
from dotenv import load_dotenv
import os

load_dotenv()


class ITelegramConfig(Protocol):
    TOKEN: str
    ID_CHAT: Optional[int]
    ID_GROUP: Optional[int]
    ID_CHANNEL: Optional[int]


class IBybitConfig(Protocol):
    PUBLIC_KEY: str
    SECRET_KEY: str
    REST_API: Optional[str]
    WSS_API: Optional[str]
    REST_TEST: Optional[str]
    WSS_TEST: Optional[str]


class ILoggerConfig(Protocol):
    LOG_LEVEL: str
    LOG_FILE: Optional[str]


@dataclass
class TelegramConfig(ITelegramConfig):
    TOKEN: str
    ID_CHAT: Optional[int] = None
    ID_GROUP: Optional[int] = None
    ID_CHANNEL: Optional[int] = None

    def __post_init__(self):
        if not self.TOKEN:
            raise ValueError("У бота должен быть установлен ТОКЕН")


@dataclass
class BybitConfig(IBybitConfig):
    PUBLIC_KEY: str
    SECRET_KEY: str
    REST_API: Optional[str] = None
    WSS_API: Optional[str] = None
    REST_TEST: Optional[str] = None
    WSS_TEST: Optional[str] = None

    def __post_init__(self):
        if not all([self.PUBLIC_KEY, self.SECRET_KEY]):
            raise ValueError(
                "Публичный и Секретный ключ для доступа к ByBit API должны быть установлены"
            )


@dataclass
class LoggerConfig(ILoggerConfig):
    LOG_LEVEL: str = "INFO"
    LOG_FILE: Optional[str] = None


def create_telegram_config() -> ITelegramConfig:
    return TelegramConfig(
        TOKEN=os.getenv("TELEGRAM_BOT_TOKEN"),
        ID_CHAT=int(env) if (env := os.getenv("TELEGRAM_ID_CHAT")) else None,
        ID_GROUP=int(env) if (env := os.getenv("TELEGRAM_ID_GROUP")) else None,
        ID_CHANNEL=int(env) if (env := os.getenv("TELEGRAM_ID_CHANNEL")) else None
    )


def create_bybit_config() -> IBybitConfig:
    return BybitConfig(
        PUBLIC_KEY=os.getenv("BYBIT_PUBLIC_KEY"),
        SECRET_KEY=os.getenv("BYBIT_SECRET_KEY"),
        REST_API=str(env) if (env := os.getenv("BYBIT_REST_API")) else None,
        WSS_API=str(env) if (env := os.getenv("BYBIT_WSS_API")) else None,
        REST_TEST=str(env) if (env := os.getenv("BYBIT_REST_TEST")) else None,
        WSS_TEST=str(env) if (env := os.getenv("BYBIT_WSS_TEST")) else None
    )


def create_logger_config() -> ILoggerConfig:
    return LoggerConfig(
        LOG_LEVEL=os.getenv("LOGGER_LOG_LEVEL"),
        LOG_FILE=os.getenv("LOGGER_LOG_FILE")
    )