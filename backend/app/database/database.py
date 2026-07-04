"""
CareerOS Database Configuration
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.core.config import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)

# Create session factory
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)