# # test_my_application.py
# from playwright.sync_api import Page

# def test_visit_admin_dashboard(page: Page):
#     '''pytest --headed pwtests.py'''
#     page.goto("https://marketmilk.babypips.com")
#     # ...
#################################################################################
# # test_my_application.py
# import pytest

# # @pytest.mark.skip_browser("firefox")
# @pytest.mark.only_browser("chromium")
# def test_visit_example(page):
#     page.goto("https://docs.scrapy.org/en/latest/topics/logging.html")
#     # ...

#################################################################################
# # conftest.py
# import pytest


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright):
#     iphone_11 = playwright.devices['iPhone 11 Pro']
#     return {
#         **browser_context_args,
#         "ignore_https_errors": True,  # Ignore HTTPS errors
#         "viewport": {     # viewport size
#             "width": 1920,
#             "height": 1080,
#         },
#         **iphone_11,  # Device emulation
#     }

#################################################################################
# # Persistent context
# # conftest.py
# import pytest
# from playwright.sync_api import BrowserType
# from typing import Dict


# @pytest.fixture(scope="session")
# def context(
#     browser_type: BrowserType,
#     browser_type_launch_args: Dict,
#     browser_context_args: Dict
# ):
#     context = browser_type.launch_persistent_context("./foobar", **{
#         **browser_type_launch_args,
#         **browser_context_args,
#         "locale": "de-DE",
#     })
#     yield context
#     context.close()

#################################################################################
# # unittest.TestCase
# import pytest
# import unittest

# from playwright.sync_api import Page


# class MyTest(unittest.TestCase):
#     @pytest.fixture(autouse=True)
#     def setup(self, page: Page):
#         self.page = page

#     def test_foobar(self):
#         self.page.goto("https://microsoft.com")
#         self.page.locator("#search").click()
#         assert self.page.evaluate("1 + 1") == 2

#################################################################################
# pdb Debugging:
import pytest
import unittest

from playwright.sync_api import Page


class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_foobar(self):
        self.page.goto("https://microsoft.com")
        self.page.locator("#search").click()
        breakpoint()
        # assert self.page.evaluate("1 + 1") == 2