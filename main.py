import asyncio
from aiohttp import ClientSession
from bot import dp, bot, commands


async def main():
    session = ClientSession()
    commands.register_handlers(session)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
