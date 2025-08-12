from aiogram import Dispatcher
from aiogram import types
from handlers.base import IHandler
from utils.logger import ILogger


class SystemCommands(IHandler):
    def __init__(self, logger: ILogger):
        self._logger = logger

    def register(self, dp: Dispatcher):
        dp.register_message_handler(
            self._cmd_start,
            commands=["start"],
            state="*"
        )
        dp.register_message_handler(
            self._cmd_help,
            commands=["help"],
            state="*"
        )

    async def _cmd_start(self, message: types.Message) -> None:
        self._logger.debug(f"Выполнение команды /start от {message.from_user.id}")
        await message.answer("Бот активен. Введите /help для получения списка команд.")

    async def _cmd_help(self, message: types.Message) -> None:
        self._logger.debug(f"Выполнение команды /help от {message.from_user.id}")
        await message.answer("Доступные команды:\n/start\n/help")


def create_system_cmd_handler(logger: ILogger) -> IHandler:
    return SystemCommands(logger)
