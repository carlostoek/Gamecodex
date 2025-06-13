from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    """Provide help information."""
    await message.answer("Send me any text and I'll echo it back.")
