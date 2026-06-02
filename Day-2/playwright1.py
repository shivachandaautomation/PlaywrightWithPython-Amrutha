# print("Shiva")
from playwright.sync_api import sync_playwright, Playwright

with sync_playwright() as playwright:
    mybrowser = playwright.firefox
    browser = mybrowser.launch(headless=False)   # 1000 ms = 1 second delay per action)
    page = browser.new_page()
    page.goto("https://automationexercise.com/login")
    
    page.screenshot(path='F:/Playwright_Project')
    title = page.title()
    assert "Exercise - Signup / Login" in title
    print(title)
    browser.close()

    # headless = True  # Default (no UI)
    # headless = False  # Opens browser UI
    # slow_mo = 1000
    # channel = "chrome"
    # channel = "msedge"
    # ignore_https_errors = True
    # timeout = 30000 #Max time to launch browser

    # launch() → Browser    level    settings
    # context() → User / session    level    settings
    # page() → Page     level    actions

