from aiogram import Bot, Dispatcher
from typing import Protocol
from config import ITelegramConfig
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
    ):
        self._config = config
        self._logger = logger
        self._bot = Bot(token=self._config.TOKEN)
        self._dp = Dispatcher(bot=self._bot)

    async def start(self) -> None:
        self._logger.info("Бот запущен")
        await self._dp.start_polling()

    async def stop(self) -> None:
        self._logger.info("Бот остановлен")
        await self._bot.close()

    def register_handlers(self, *modules) -> None:
        for module in modules:
            if hasattr(module, "register"):
                module.register(self._dp)
                self._logger.debug(
                    f"Зарегистрирован обработчик из {module.__name__}"
                )


def create_bot(
    config: ITelegramConfig,
    logger: ILogger,
    handlers: tuple
) -> IBotClient:
    bot = TelegramBot(config, logger)
    bot.register_handlers(*handlers)
    return bot
