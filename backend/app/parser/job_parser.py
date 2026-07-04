"""
CareerOS Universal Job Parser
"""

from bs4 import Tag


class JobParser:

    def parse(self, card: Tag):

        return {

            "title": self.title(card),

            "location": self.location(card),

            "link": self.link(card)

        }

    def title(self, card: Tag):

        for tag in ["h1", "h2", "h3", "h4", "a"]:

            element = card.find(tag)

            if element:

                text = element.get_text(strip=True)

                if text:

                    return text

        return ""

    def location(self, card: Tag):

        text = card.get_text(" ", strip=True)

        keywords = [
            "Remote",
            "Bangalore",
            "Bengaluru",
            "Hyderabad",
            "Pune",
            "Chennai",
            "Mumbai",
            "Delhi",
            "India"
        ]

        for city in keywords:

            if city.lower() in text.lower():

                return city

        return ""

    def link(self, card: Tag):

        anchor = card.find("a")

        if anchor:

            return anchor.get("href", "")

        return ""


job_parser = JobParser()