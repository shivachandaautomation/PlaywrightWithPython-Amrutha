from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        # Launch browser (Chromium / Chrome)
        browser = p.chromium.launch(headless=False)

        # Create new browser context
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        # Navigate to URL
        page.goto("https://www.google.com")

        # Verify title
        assert "Google" in page.title()
        print("Title is:", page.title())

        # Close browser
        browser.close()

test_google()
