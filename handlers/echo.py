from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_all(message: Message) -> None:
    """Echo back any received text message."""
    if message.text:
        await message.answer(message.text)
