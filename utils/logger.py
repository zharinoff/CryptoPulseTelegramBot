import logging
from typing import Protocol
from config import ILoggerConfig


class ILogger(Protocol):
    def debug(self, msg: str) -> None: ...

    def info(self, msg: str) -> None: ...

    def warning(self, msg: str) -> None: ...

    def error(self, msg: str) -> None: ...


class Logger(ILogger):
    def __init__(self, config: ILoggerConfig):
        self._logger = logging.getLogger("CryptoPulse")
        self._configure(config)

    def _configure(self, config: ILoggerConfig) -> None:
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self._logger.addHandler(console_handler)

        if config.LOG_FILE is not None:
            file_handler = logging.FileHandler(config.LOG_FILE)
            file_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)

        log_level = config.LOG_LEVEL #if config.LOG_LEVEL else "INFO"
        self._logger.setLevel(log_level)

    def debug(self, msg: str) -> None:
        self._logger.debug(msg)

    def info(self, msg: str) -> None:
        self._logger.info(msg)

    def warning(self, msg: str) -> None:
        self._logger.warning(msg)

    def error(self, msg: str) -> None:
        self._logger.error(msg)


def create_logger(config: ILoggerConfig) -> ILogger:
    return Logger(config)
