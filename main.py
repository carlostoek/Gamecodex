"""Entry point for running the Telegram bot."""
import asyncio

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot import bot, dp

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    """Handle the /start command."""
    await message.answer("Hello, I'm alive!")

async def main() -> None:
    """Start the bot."""
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
