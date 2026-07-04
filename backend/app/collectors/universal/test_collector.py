from backend.app.browser.core.browser import browser_service

from backend.app.parser.html_parser import html_parser

from backend.app.collectors.universal.extractor import extractor

page = browser_service.start()

browser_service.goto("https://example.com")

html = browser_service.html()

browser_service.close()

soup = html_parser.parse(html)

jobs = extractor.extract(soup)

print(jobs)