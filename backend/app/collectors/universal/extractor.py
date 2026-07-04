"""
CareerOS Universal Extractor
"""

from backend.app.parser.job_parser import job_parser


class UniversalExtractor:

    def extract(self, soup):

        jobs = []

        selectors = [
            "div",
            "article",
            "li"
        ]

        for selector in selectors:

            cards = soup.find_all(selector)

            for card in cards:

                job = job_parser.parse(card)

                if job["title"]:

                    jobs.append(job)

        return jobs


extractor = UniversalExtractor()