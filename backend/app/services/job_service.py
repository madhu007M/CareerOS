"""
CareerOS Job Service
"""

from sqlalchemy.orm import Session

from backend.app.schemas.job import JobCreate
from backend.app.repositories.job_repository import job_repository


class JobService:

    def create_job(self, db: Session, job: JobCreate):

        return job_repository.create(db, job)

    def get_jobs(self, db: Session):

        return job_repository.get_all(db)

    def get_job(self, db: Session, job_id: int):

        return job_repository.get_by_id(db, job_id)

    def delete_job(self, db: Session, job_id: int):

        return job_repository.delete(db, job_id)


job_service = JobService()