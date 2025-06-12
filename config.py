"""Bot configuration module."""
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class Settings:
    """Application settings loaded from environment variables."""
    bot_token: str

def load_settings() -> Settings:
    """Read settings from environment variables."""
    return Settings(
        bot_token=os.getenv("BOT_TOKEN", "")
    )

settings = load_settings()
