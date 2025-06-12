"""Initialization of the Bot and Dispatcher."""
"""Initialization of the Bot"""

from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.memory import MemoryStorage

from config import settings

bot = Bot(token=settings.bot_token, parse_mode="HTML")

# Dispatcher is responsible for managing updates

dp = Dispatcher(storage=MemoryStorage())
