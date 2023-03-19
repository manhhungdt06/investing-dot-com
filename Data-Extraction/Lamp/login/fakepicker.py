from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(storage_state="investate.json")

    page = context.new_page()
    page.goto("https://www.investing.com")

    page.wait_for_timeout(2000)
    page.goto("https://www.investing.com/indices/bovespa-historical-data")
    page.wait_for_timeout(1000)
    page.locator(".DatePickerWrapper_icon__Qw9f8").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox").nth(1).fill("2000-01-22")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Apply").click()
    # no need fake mouse moving, just waiting their html finish loading
    page.wait_for_timeout(50000)

    page.pause()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
