from aiogram.filters import Command
from aiogram.types import Message
from functools import partial

from bot import dp, logger
from handlers.messages import START_MSG, ERROR_MSG


async def cmd_start(message: Message) -> None:
    try:
        await message.answer(START_MSG)
        logger.info(f"Новый пользователь: {message.from_user.id}")
    except Exception as e:
        logger.error(f"Ошибка в команде /start: {e}")
        await message.answer(ERROR_MSG)


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


async def cmd_send_price(message: Message, coin: str):
    try:
        await message.answer(
            f"Цена {coin}: <b>XXX</b> (в разработке)",
            parse_mode="HTML"
        )
    except Exception as e:
        logger.error(f"Ошибка в команде /send_price: {e}")
        await message.answer(ERROR_MSG)


async def unknown_command(message: Message) -> None:
    await message.answer(f"Неизвестная команда. {START_MSG}")

def register_handlers():
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_chat_id, Command("chat_id"))
    dp.message.register(partial(cmd_send_price, coin="BTC"), Command("btc"))
    dp.message.register(partial(cmd_send_price, coin="ETH"), Command("eth"))
    dp.message.register(unknown_command)


__all__ = [dp]