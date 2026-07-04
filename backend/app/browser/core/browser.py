"""
CareerOS Browser Engine
"""

from playwright.sync_api import sync_playwright


class BrowserService:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self, headless=False):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=headless
        )

        self.page = self.browser.new_page()

        return self.page

    def goto(self, url: str):
        self.page.goto(url)

    def title(self):
        return self.page.title()

    def html(self):
        return self.page.content()

    def text(self, selector: str):
        return self.page.locator(selector).inner_text()

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str):
        self.page.locator(selector).fill(value)

    def wait(self, milliseconds=2000):
        self.page.wait_for_timeout(milliseconds)

    def close(self):
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()


browser_service = BrowserService()