# '''
import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        # Start tracing before creating / navigating a page.
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()   # storage_state="auth.json"
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.goto("https://www.babypips.com")

        # Step by step
        await page.get_by_role("navigation").get_by_role("link", name="MarketMilk™").click()
        await page.get_by_role("button", name="Price Stream").click()
        await page.get_by_role("option", name="Last Closed").click()
        await page.get_by_role("button", name="Time Interval").click()
        await page.get_by_role("option", name="1W").click()
        await page.get_by_role("region", name="Currency Strength Meter").get_by_role("link", name="NZD NZD").click()
        await page.get_by_role("button", name="Base Currency").click()
        await page.get_by_role("option", name="Normalize").click()
        await page.get_by_role("link", name="Performance").click()
        await page.get_by_role("radio", name="30D").click()
        await page.get_by_role("link", name="Heat Map").click()
        await page.get_by_role("link", name="Overbought / Sold").click()
        await page.get_by_role("region", name="RSI").get_by_role("switch").click()
        await page.get_by_role("region", name="Stochastic").get_by_role("switch").click()
        await page.get_by_role("region", name="Williams %R").get_by_role("switch").click()
        await page.get_by_role("region", name="Bollinger Bands").get_by_role("switch").click()
        await page.get_by_role("region", name="Keltner Channel").get_by_role("switch").click()
        # End Step by step
         
        # # Stop tracing and export it into a zip archive.
        # await context.tracing.stop(path="trace.zip")

asyncio.run(main())
# '''

'''
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.babypips.com")

    page.wait_for_timeout(300)
    page.get_by_role("link", name="Sign In").click()
    page.wait_for_timeout(300)
    page.get_by_placeholder("Email or Username").click()
    page.wait_for_timeout(300)
    page.get_by_placeholder("Email or Username").fill("scofield12491@gmail.com")
    page.wait_for_timeout(300)
    page.get_by_placeholder("Email or Username").press("Tab")
    page.wait_for_timeout(300)
    page.get_by_placeholder("Password").fill("Blockch@in91")
    page.wait_for_timeout(300)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(300)
    page.get_by_role("navigation").get_by_role("link", name="MarketMilk™").click()
    page.wait_for_timeout(300)
    page.get_by_role("button", name="Price Stream").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="Last Closed").click()
    page.wait_for_timeout(300)
    page.get_by_role("button", name="Time Interval").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="1W").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Currency Strength Meter").get_by_role("link", name="NZD NZD").click()
    page.wait_for_timeout(300)
    page.get_by_role("button", name="Base Currency").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="Normalize").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Performance").click()
    page.wait_for_timeout(300)
    page.get_by_role("radio", name="30D").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Heat Map").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Overbought / Sold").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="RSI").get_by_role("switch").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Stochastic").get_by_role("switch").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Williams %R").get_by_role("switch").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Bollinger Bands").get_by_role("switch").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Keltner Channel").get_by_role("switch").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Trend Matrix").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Trend Strength (Short-Term)").get_by_role("button", name="Cross Selector").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="20 EMA").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Trend Strength (Short-Term)").get_by_role("button", name="Base Selector").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="50 EMA").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Moving Averages").click()
    page.wait_for_timeout(300)
    page.get_by_role("switch").click()
    page.wait_for_timeout(300)
    page.get_by_role("button", name="Filter (4)").click()
    page.wait_for_timeout(300)
    page.locator("div").filter(has_text="10").click()
    page.wait_for_timeout(300)
    page.locator("div").filter(has_text="100").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Price Deviation from MAs").get_by_role("button", name="EMA").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Is Price Above/Below Its Moving Average?").get_by_role("button", name="EMA").click()
    page.wait_for_timeout(300)
    page.get_by_role("button", name="Filter (2)").click()
    page.wait_for_timeout(300)
    page.locator("div").filter(has_text="100").click()
    page.wait_for_timeout(300)
    page.locator("div").filter(has_text="20").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Volatility").click()
    page.wait_for_timeout(300)
    page.get_by_role("radio", name="30D").click()
    page.wait_for_timeout(300)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
# '''

'''
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # storage_state="auth.json"
    page = context.new_page()
    page.goto("https://www.babypips.com")
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Sign In").click()
    page.wait_for_timeout(300)
    page.get_by_placeholder("Email or Username").click()
    page.wait_for_timeout(300)
    page.get_by_placeholder("Email or Username").fill("scofield12491@gmail.com")
    page.wait_for_timeout(300)
    page.get_by_placeholder("Email or Username").press("Tab")
    page.wait_for_timeout(300)
    page.get_by_placeholder("Password").fill("Blockch@in91")
    page.wait_for_timeout(300)
    page.get_by_placeholder("Password").press("Enter")
    page.wait_for_timeout(300)
    page.get_by_role("navigation").get_by_role("link", name="MarketMilk™").click()
    page.wait_for_timeout(300)

    # context.storage_state(path="authVN.json")

    page.get_by_role("button", name="Time Interval").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="1W").click()
    page.wait_for_timeout(300)
    page.get_by_role("button", name="Price Stream").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name="Last Closed").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Currency Strength Meter").get_by_role("link", name="EUR EUR").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Performance").click()
    page.wait_for_timeout(300)
    page.get_by_role("radio", name="30D").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Heat Map").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Overbought / Sold").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="RSI").get_by_role("switch").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Stochastic").get_by_role("switch").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Williams %R").get_by_role("switch").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Bollinger Bands").get_by_role("switch").click()
    page.wait_for_timeout(300)
    page.get_by_role("region", name="Keltner Channel").get_by_role("radio", name="Show Values").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Trend Matrix").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Moving Averages").click()
    page.wait_for_timeout(300)
    page.get_by_role("radio", name="Show Values").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Volatility").click()
    page.wait_for_timeout(300)
    page.get_by_role("radio", name="30D").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="EUR USD EUR/USD").click()
    page.wait_for_timeout(300)
    page.get_by_role("button", name="All Sessions").click()
    page.wait_for_timeout(1000)
    page.get_by_text("London").click()
    page.wait_for_timeout(300)
    # page.locator("div").filter(has_text="New York").click()   # error this
    page.get_by_text("New York").click()
    page.wait_for_timeout(300)

    # page.get_by_role("button", name="Sessions (2)").click()
    # page.wait_for_timeout(300)

    page.get_by_role("link", name="Pivot Points").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="? Buy or Sell?").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Performance").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Overbought / Sold").click()
    page.wait_for_timeout(300)
    page.get_by_role("link", name="Trend").click()
    page.wait_for_timeout(300)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
# '''