"""
CareerOS
Collector Manager
"""

from typing import List
from scripts.core.base_collector import BaseCollector


class CollectorManager:

    def __init__(self):
        self.collectors: List[BaseCollector] = []

    def register(self, collector: BaseCollector):
        self.collectors.append(collector)

    def get_collectors(self):
        return self.collectors