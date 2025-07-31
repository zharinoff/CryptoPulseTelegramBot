from aiogram.filters import Command
from aiogram.types import Message

from . import dp, logger
from .messages import START_MSG, ERROR_MSG


@dp.message(Command("start"))
async def cmd_start(message: Message) -> None:
    try:
        await message.answer(START_MSG)
        logger.info(f"Новый пользователь: {message.from_user.id}")
    except Exception as e:
        logger.error(f"Ошибка в команде /start: {e}")
        await message.answer(ERROR_MSG)


@dp.message(Command("chat_id"))
async def cmd_chat_id(message: Message) -> None:
    try:
        chat_type = "группы" if message.chat.type != "private" else "чата"
        await message.answer(
            f"ID {chat_type}: <code>{message.chat.id}</code>",
            parse_mode="HTML"
        )
    except Exception as e:
        logger.error(f"Ошибка в команде /chat_id: {e}")
        await message.answer(ERROR_MSG)


@dp.message(Command("btc"))
async def cmd_btc(message: Message) -> None:
    try:
        await message.answer(
            "Цена на биток: <b>***</b> (в разработке)",
            parse_mode="HTML"
        )
    except Exception as e:
        logger.error(f"Ошибка в команде /btc: {e}")
        await message.answer(ERROR_MSG)


@dp.message(Command("eth"))
async def cmd_eth(message: Message) -> None:
    try:
        await message.answer(
            "Цена на эфир: <b>***</b> (в разработке)",
            parse_mode="HTML"
        )
    except Exception as e:
        logger.error(f"Ошибка в команде /eth: {e}")
        await message.answer(ERROR_MSG)


@dp.message()
async def unknown_command(message: Message) -> None:
    await message.answer(f"Неизвестная команда. {START_MSG}")

__all__ = [dp]
