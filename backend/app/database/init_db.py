"""
CareerOS Database Initialization
"""

from backend.app.database.database import engine
from backend.app.database.base import Base

# Import all models here
from backend.app.models.job import Job
from backend.app.models.company import Company


def init_db():
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)