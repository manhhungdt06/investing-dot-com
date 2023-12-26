# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://marketmilk.babypips.com")
#     print(page.title())
#     browser.close()

######################################################################
# import asyncio
# from playwright.async_api import async_playwright

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto("https://marketmilk.babypips.com")
#         print(await page.title())
#         await browser.close()

# asyncio.run(main())

######################################################################
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # browser = p.webkit.launch(headless=False)
    browser = p.chromium.launch(headless=False, slow_mo=50)
    # browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    page.screenshot(path="example.png")
    browser.close()


######################################################################
# Pyinstaller???
'''
PLAYWRIGHT_BROWSERS_PATH=0 playwright install chromium
pyinstaller -F main.py
'''
# page.wait_for_timeout(5000) instead of time.sleep(5)