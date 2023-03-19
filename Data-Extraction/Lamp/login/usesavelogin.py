from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(storage_state="investate.json")

    page = context.new_page()
    page.goto("https://www.investing.com")

    page.wait_for_timeout(2000)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)