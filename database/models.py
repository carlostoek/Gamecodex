from __future__ import annotations

from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class User(Base):
    """SQLAlchemy User model."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    join_date = Column(DateTime, default=datetime.utcnow)
