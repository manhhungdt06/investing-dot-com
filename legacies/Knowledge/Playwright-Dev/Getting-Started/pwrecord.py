import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Make sure to run headed.
        browser = await p.chromium.launch(headless=False)

        # Setup context however you like.
        context = await browser.new_context() # Pass any options
        await context.route('**/*', lambda route: route.continue_())

        # Pause the page, and start recording manually ??? what to record
        page = await context.new_page()
        await page.pause()

asyncio.run(main())

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     # Make sure to run headed.
#     browser = p.chromium.launch(headless=False)

#     # Setup context however you like.
#     context = browser.new_context() # Pass any options
#     context.route('**/*', lambda route: route.continue_())

#     # Pause the page, and start recording manually.
#     page = context.new_page()
#     page.pause()