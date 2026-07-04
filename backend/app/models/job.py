"""
Job Model
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.database.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    title = Column(String, nullable=False)

    location = Column(String)

    platform = Column(String)

    url = Column(String)

    description = Column(String)

    salary = Column(String)

    employment_type = Column(String)

    posted_date = Column(String)

    company = relationship("Company", back_populates="jobs")