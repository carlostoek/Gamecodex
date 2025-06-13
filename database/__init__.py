"""Database related modules."""

from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .db import init_db, add_user, DB_PATH
from .models import Base

engine = create_engine(f"sqlite:///{DB_PATH}", future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_session():
    """Initialize database tables and provide a session."""
    Base.metadata.create_all(engine)
    return SessionLocal()

__all__ = ["init_db", "add_user", "get_session", "SessionLocal", "engine"]
