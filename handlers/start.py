from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Respond to the /start command."""
    await message.answer("Hello! I'm alive!")

@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    """Provide help information."""
    await message.answer("Send me any text and I'll echo it back.")
