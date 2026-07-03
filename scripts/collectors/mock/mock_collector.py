"""
CareerOS
Mock Collector
"""

from scripts.core.base_collector import BaseCollector


class MockCollector(BaseCollector):

    def __init__(self):
        super().__init__("Mock Collector")

    def search_jobs(self, keyword: str, location: str):

        return [

            {
                "company": "Google",
                "role": "Cyber Security Intern",
                "location": "Bangalore"
            },

            {
                "company": "Microsoft",
                "role": "SOC Analyst Intern",
                "location": "Hyderabad"
            },

            {
                "company": "Cisco",
                "role": "Security Engineer Intern",
                "location": "Bangalore"
            }

        ]