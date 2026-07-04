"""
CareerOS Job Repository
"""

from sqlalchemy.orm import Session

from backend.app.models.job import Job
from backend.app.schemas.job import JobCreate
from backend.app.repositories.company_repository import company_repository


class JobRepository:

    def create(self, db: Session, job: JobCreate):

        company = company_repository.get_or_create(
            db,
            job.company
        )

        db_job = Job(
            company_id=company.id,
            title=job.title,
            location=job.location,
            platform=job.platform,
            url=job.url,
            description="",
            salary="",
            employment_type="",
            posted_date=""
        )

        db.add(db_job)
        db.commit()
        db.refresh(db_job)

        return db_job

    def get_all(self, db: Session):
        return db.query(Job).all()

    def get_by_id(self, db: Session, job_id: int):
        return db.query(Job).filter(Job.id == job_id).first()

    def delete(self, db: Session, job_id: int):

        job = self.get_by_id(db, job_id)

        if job:
            db.delete(job)
            db.commit()

        return job


job_repository = JobRepository()