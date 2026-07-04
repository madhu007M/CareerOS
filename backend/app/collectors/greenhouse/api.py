"""
Greenhouse API Client
"""

from typing import List

import httpx

from backend.app.schemas.job import JobCreate


class GreenhouseAPI:

    BASE_URL = "https://boards-api.greenhouse.io/v1/boards"

    def fetch_jobs(self, board: str) -> List[JobCreate]:

        url = f"{self.BASE_URL}/{board}/jobs"

        response = httpx.get(
            url,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        jobs = []

        for item in data.get("jobs", []):

            jobs.append(
                JobCreate(
                    company=board.title(),
                    title=item.get("title", ""),
                    location=item.get("location", {}).get("name", ""),
                    platform="Greenhouse",
                    url=item.get("absolute_url", "")
                )
            )

        return jobs


greenhouse_api = GreenhouseAPI()