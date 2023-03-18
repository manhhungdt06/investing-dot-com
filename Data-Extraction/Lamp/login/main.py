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
    page.goto("https://www.investing.com")
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Sign In").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Email").click()
    page.wait_for_timeout(500)
    page.get_by_placeholder("Email").fill(config_data['username'])
    page.wait_for_timeout(500)
    page.get_by_placeholder("Email").press("Tab")
    page.wait_for_timeout(500)
    page.get_by_placeholder("Password").fill(config_data['password'])
    page.wait_for_timeout(500)
    page.get_by_placeholder("Password").press("Enter")
    page.wait_for_timeout(500)
    page.get_by_role("link", name="Investing.com - Financial Markets Worldwide").click()
    page.wait_for_timeout(1000)
    # ---------------------
    context.storage_state(path="invest_auth.json")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
