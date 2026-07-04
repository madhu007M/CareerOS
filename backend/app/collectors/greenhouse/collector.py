"""
Greenhouse Collector
"""

from backend.app.collectors.base.base_collector import BaseCollector


class GreenhouseCollector(BaseCollector):

    def __init__(self):

        super().__init__("Greenhouse")

    def collect(self):

        print("Greenhouse Collector Started")

        return []