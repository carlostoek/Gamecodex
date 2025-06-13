"""Database related modules."""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

DB_PATH = Path("database/bot.db")


@contextmanager
def get_session() -> Iterator[sqlite3.Connection]:
    """Yield a SQLite connection for database operations."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()


from .db import init_db, add_user  # noqa: E402

__all__ = ["init_db", "add_user", "get_session", "DB_PATH"]

