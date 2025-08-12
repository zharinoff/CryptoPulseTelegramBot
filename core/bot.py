from aiogram import Bot, Dispatcher
from typing import Protocol, Iterable
from config import ITelegramConfig
from handlers.base import IHandler
from utils.logger import ILogger


class IBotClient(Protocol):
    async def start(self) -> None: ...
    async def stop(self) -> None: ...
    def register_handlers(self) -> None: ...


class TelegramBot(IBotClient):
    def __init__(
            self,
            config: ITelegramConfig,
            logger: ILogger,
            handlers: Iterable[IHandler]
    ):
        self._config = config
        self._logger = logger
        self._bot = Bot(token=self._config.TOKEN)
        self._dp = Dispatcher(bot=self._bot)
        self._handlers = handlers

    async def start(self) -> None:
        self._logger.info("Бот запущен")
        await self._dp.start_polling(self._bot)

    async def stop(self) -> None:
        self._logger.info("Бот остановлен")
        await self._bot.session.close()

    def register_handlers(self) -> None:
        for handler in self._handlers:
            handler.register(dp=self._dp)
            self._logger.debug(
                f"Зарегистрирован обработчик {handler.__class__.__name__}"
            )


def create_bot(
    config: ITelegramConfig,
    logger: ILogger,
    handlers: Iterable[IHandler]
) -> IBotClient:
    bot = TelegramBot(config, logger, handlers)
    bot.register_handlers()
    return bot
