"""Aggregates all bot routes"""

from aiogram import Dispatcher

from .user import start

from . import help, echo

def register_handlers(dp: Dispatcher):

    """Include all bot handlers"""

    dp.include_router(start.router)

    dp.include_router(help.router)

    dp.include_router(echo.router)
