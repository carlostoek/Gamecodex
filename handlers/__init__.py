"""Aggregates all bot routers."""
from aiogram import Dispatcher

from .user import start
from . import help, echo


def register_handlers(dp: Dispatcher) -> None:
    """Include all routers in the dispatcher."""
    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(echo.router)
