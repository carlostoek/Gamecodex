"""Initialization of the Bot and Dispatcher."""
from aiogram import Bot, Dispatcher

from config import settings

bot = Bot(token=settings.bot_token, parse_mode="HTML")
# Dispatcher is responsible for handling updates
dp = Dispatcher()
