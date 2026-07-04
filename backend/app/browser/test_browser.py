from backend.app.browser.core.browser import browser_service

browser = browser_service.start()

page = browser.new_page()

page.goto("https://www.google.com")

print(page.title())

page.wait_for_timeout(5000)

browser_service.stop()