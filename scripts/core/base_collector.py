"""
CareerOS
Base Collector
"""

from abc import ABC, abstractmethod


class BaseCollector(ABC):
    """
    Base class for all job collectors.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def search_jobs(self, keyword: str, location: str):
        """
        Search jobs from the platform.
        """
        pass