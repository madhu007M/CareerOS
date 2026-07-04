from backend.app.browser.core.browser import browser_service

page = browser_service.start()

browser_service.goto("https://example.com")

print(browser_service.title())

browser_service.wait(3000)

browser_service.close()