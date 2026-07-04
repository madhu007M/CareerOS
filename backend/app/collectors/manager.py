"""
CareerOS Collector Manager
"""

from backend.app.collectors.google.collector import GoogleCollector


class CollectorManager:

    def __init__(self):

        self.collectors = [
            GoogleCollector(),
        ]

    def collect_all_jobs(self):

        jobs = []

        for collector in self.collectors:

            print(f"Running {collector.__class__.__name__}")

            jobs.extend(
                collector.collect_jobs()
            )

        return jobs