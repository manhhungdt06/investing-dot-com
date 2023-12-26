import re
from playwright.sync_api import Page, expect
import pytest


# def test_intro_page(page: Page):                          # fucking test_ prefix for pytest
#     page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

#     # create a locator
#     get_started = page.get_by_role("link", name="Get started")

#     # Expect an attribute "to be strictly equal" to the value.
#     expect(get_started).to_have_attribute("href", "/docs/intro")        # to_have_attribute???

#     # Click the get started link.
#     get_started.click()

#     # Expects the URL to contain intro.
#     expect(page).to_have_url(re.compile(".*intro"))                     # to_have_url???


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    '''mainly modify this function'''
    print("beforeEach")
    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    # page.goto("https://playwright.dev/python/docs/writing-tests")
    yield
    print("afterEach")


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/")
    # expect(page).to_have_url("https://playwright.dev/python/docs/writing-tests")
