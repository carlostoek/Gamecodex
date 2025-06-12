"""Aggregates all bot routers."""
from aiogram import Dispatcher

from . import start, echo


def register_handlers(dp: Dispatcher) -> None:
    """Include all routers in the dispatcher."""
    dp.include_router(start.router)
    dp.include_router(echo.router)
