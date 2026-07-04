"""
Google Collector
"""

from backend.app.collectors.base.collector import BaseCollector


class GoogleCollector(BaseCollector):

    def collect_jobs(self):

        return [
            {
                "company": "Google",
                "title": "Cyber Security Intern",
                "location": "Bangalore",
                "platform": "Google Careers",
                "url": "https://careers.google.com"
            }
        ]