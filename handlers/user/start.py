from __future__ import annotations

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import asyncio

from database.db import add_user

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Handle the /start command with a welcome and user save."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Profile", callback_data="profile"),
            InlineKeyboardButton(text="Help", callback_data="help"),
            InlineKeyboardButton(text="Level", callback_data="level"),
        ]
    ])

    join_date = datetime.utcnow().isoformat()
    await asyncio.to_thread(
        add_user,
        message.from_user.id,
        message.from_user.username,
        join_date,
    )

    await message.answer("Welcome to the bot!", reply_markup=keyboard)
