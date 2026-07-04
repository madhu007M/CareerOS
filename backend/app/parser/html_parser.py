"""
CareerOS HTML Parser
"""

from bs4 import BeautifulSoup


class HTMLParser:

    def parse(self, html: str):

        return BeautifulSoup(
            html,
            "lxml"
        )


html_parser = HTMLParser()