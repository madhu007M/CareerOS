"""
Company Model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.app.database.base import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, nullable=False)

    website = Column(String)

    career_page = Column(String)

    industry = Column(String)

    location = Column(String)

    logo = Column(String)

    jobs = relationship(
        "Job",
        back_populates="company",
        cascade="all, delete"
    )