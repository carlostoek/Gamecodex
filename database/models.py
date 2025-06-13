"""Data models for the database."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class User:
    """Representation of a bot user."""

    id: int
    username: str | None
    full_name: str | None
    join_date: datetime

