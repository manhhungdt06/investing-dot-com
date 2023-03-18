'''
from playwright.sync_api import Playwright, sync_playwright, expect
from configparser import ConfigParser
from pathlib import Path
current_folder = Path(__file__).parent.resolve()

def run(playwright: Playwright) -> None:

    # Loading user info
    config = ConfigParser()
    config.read(f"{current_folder}/accounts.ini")
    user = input("What is your name?: ")
    try:
        config_data = config[user]
    except:
        print("User not found!")
        exit(0)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.babypips.com")
    page.wait_for_timeout(500)
    page.get_by_role("link", name="Sign In").click()
    page.wait_for_timeout(500)
    page.get_by_placeholder("Email or Username").click()
    page.wait_for_timeout(500)
    page.get_by_placeholder("Email or Username").fill(config_data['username'])
    page.wait_for_timeout(500)
    page.get_by_placeholder("Password").click()
    page.wait_for_timeout(500)
    page.get_by_placeholder("Password").fill(config_data['password'])
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(500)
    page.get_by_role("navigation").get_by_role("link", name="MarketMilk™").click()
    page.wait_for_timeout(300)
    
    # ---------------------
    context.storage_state(path="auth.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
# '''

# ######################################################################
# '''
# ----------------------- USING SAVE INFO 
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    page.wait_for_timeout(1000)
    page.goto("https://www.babypips.com")
    page.wait_for_timeout(500)
    page.get_by_role("navigation").get_by_role("link", name="MarketMilk™").click()
    page.wait_for_timeout(500)
    # ---------------------
    # page.pause()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
# '''