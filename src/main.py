import asyncio
from bot import dp, bot, commands


async def main():
    commands.register_handlers()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
