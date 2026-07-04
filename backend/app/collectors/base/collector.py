"""
Base Collector Interface
"""

from abc import ABC, abstractmethod


class BaseCollector(ABC):

    @abstractmethod
    def collect_jobs(self):
        """
        Collect jobs from a platform.

        Returns:
            list[dict]
        """
        pass