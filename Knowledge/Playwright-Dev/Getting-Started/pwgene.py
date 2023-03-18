# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(timezone_id="Europe/Paris")
#     page = context.new_page()
#     page.goto("https://www.babypips.com/")
#     page.get_by_role("link", name="Sign In").click()
#     page.get_by_placeholder("Email or Username").click()
#     page.get_by_placeholder("Email or Username").fill("scofield12491@gmail.com")
#     page.get_by_placeholder("Password").click()
#     page.get_by_placeholder("Password").fill("Blockch@in91")
#     page.get_by_role("button", name="Sign In").click()

#     # ---------------------
#     context.storage_state(path="authEU2.json")
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)

# ----------------------- USING SAVE INFO 
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="authEU2.json")
    page = context.new_page()
    
    page.goto("https://www.babypips.com/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
