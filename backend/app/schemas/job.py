"""
CareerOS Job Schemas
"""

from pydantic import BaseModel, ConfigDict


class CompanyResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class JobCreate(BaseModel):
    company: str
    title: str
    location: str
    platform: str
    url: str


class JobResponse(BaseModel):
    id: int

    company: CompanyResponse

    title: str
    location: str
    platform: str
    url: str

    description: str
    salary: str
    employment_type: str
    posted_date: str

    model_config = ConfigDict(from_attributes=True)


class JobUpdate(BaseModel):
    company: str | None = None
    title: str | None = None
    location: str | None = None
    platform: str | None = None
    url: str | None = None