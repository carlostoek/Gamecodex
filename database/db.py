"""SQLite helper functions."""
from __future__ import annotations

import sqlite3
from pathlib import Path

DB_PATH = Path("database/bot.db")


def init_db() -> None:
    """Initialize the database and create required tables."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            "id INTEGER PRIMARY KEY, "
            "username TEXT, "
            "full_name TEXT, "
            "join_date TEXT"
            ")"
        )
        conn.commit()


def add_user(
    user_id: int, username: str | None, full_name: str | None, join_date: str
) -> None:
    """Insert or update a user in the database."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO users (id, username, full_name, join_date)"
            " VALUES (?, ?, ?, ?)",
            (user_id, username, full_name, join_date),
        )
        conn.commit()
