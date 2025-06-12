"""Entry point for running the Telegram bot."""
import asyncio

from bot import bot, dp
from handlers import register_handlers
from utils.logger import setup_logging


async def main() -> None:
    """Configure and launch the bot."""
    setup_logging()
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
