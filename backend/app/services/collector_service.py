"""
CareerOS Collector Service
"""

from backend.app.collectors.manager import CollectorManager
from backend.app.database.database import SessionLocal
from backend.app.schemas.job import JobCreate
from backend.app.services.job_service import job_service


class CollectorService:

    def collect_jobs(self):

        manager = CollectorManager()

        jobs = manager.collect_all_jobs()

        db = SessionLocal()

        saved = 0

        try:

            for job in jobs:

                job_schema = JobCreate(**job)

                job_service.create_job(db, job_schema)

                saved += 1

        finally:

            db.close()

        return saved


collector_service = CollectorService()