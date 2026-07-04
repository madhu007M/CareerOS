"""
CareerOS Base Collector
"""

from abc import ABC, abstractmethod
from typing import List

from backend.app.schemas.job import JobCreate


class BaseCollector(ABC):

    def __init__(self, platform: str):
        self.platform = platform

    @abstractmethod
    def collect(self) -> List[JobCreate]:
        """
        Collect jobs from the platform.
        """
        pass