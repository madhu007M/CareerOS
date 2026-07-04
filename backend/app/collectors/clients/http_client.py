"""
CareerOS HTTP Client
"""

import requests


class HTTPClient:

    def __init__(self):

        self.headers = {
            "User-Agent":
            "CareerOS/1.0"
        }

    def get(self, url: str):

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        return response


http_client = HTTPClient()