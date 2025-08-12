from config import (
    create_telegram_config,
    create_logger_config
)
from core.bot import create_bot
from handlers.system_cmd import create_system_cmd_handler
from utils.logger import create_logger


class BotRunner:
    def __init__(self):
        self._logger = create_logger(config=create_logger_config())
        self._bot = create_bot(
            config=create_telegram_config(),
            logger=self._logger,
            handlers=[
                create_system_cmd_handler(self._logger),
            ]
        )

    async def run(self) -> None:
        self._logger.info("Запуск runner")
        try:
            await self._bot.start()
        except Exception as e:
            self._logger.error(f"Ошибка {e}")
            await self._bot.stop()


async def run() -> None:
    await BotRunner().run()