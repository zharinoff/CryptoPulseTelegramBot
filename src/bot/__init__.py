import logging
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=os.getenv("TG_BOT_TOKEN"))
dp = Dispatcher()

from . import commands

__all__ = ["bot", "dp", "commands"]