import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(storage_state="auth.json")
        page = await context.new_page()
        await page.goto("https://socolive10.tv")
        await page.wait_for_timeout(5000)
asyncio.run(main())
