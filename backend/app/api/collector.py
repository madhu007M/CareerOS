"""
Collector API
"""

from fastapi import APIRouter

from backend.app.services.collector_service import collector_service

router = APIRouter(
    prefix="/collector",
    tags=["Collector"]
)


@router.post("/run")
def run_collector():

    total = collector_service.collect_jobs()

    return {
        "message": f"{total} jobs collected successfully."
    }