# Keep those libs
from scrapy import Request, Spider
import os
import re
# import json
from datetime import datetime
from crawldata.items import IndexItem
from crawldata.settings import LOG_PATH
# End libs
from crawldata.functions import *
from crawldata.settings import COOKIES_FILE


def get_vol(string: object = None) -> str:
    return str(int(float(re.sub(r"([^0-9.])", "", str(string).strip()))*1e6)) if string and 'M' in string else ""
    

def get_number(string: object = None) -> str:
    return re.sub(r"([^0-9.])", "", str(string).strip()) if string else ""


def get_time(days: str = None) -> str:
    return datetime.strptime(days, '%m/%d/%Y').strftime('%Y-%m-%d') if days else ""


def fill_quote(string: str = None) -> str:
    return f"https://www.investing.com/indices/{string}-historical-data" if string else ""


def ext_quote(string: str = None) -> str:
    return string.replace("https://www.investing.com/indices/", "").replace("-historical-data", "") if string else ""


QUOTES = {
    "bovespa": "IBOV",
    # "brazil-index": "IBXX",
    # "brazil-index-50": "IBXL",
    # "brazil-broad-based": "IBRA",
    # "corporate-gov-stocks": "IGCX",
    # "tag-along-index": "ITAG",
    # "corporate-governance-igcnm": "IGNM",
    # "corporate-gov-trade": "IGCT",
    # "bovespa-dividend": "IDIV",
    # "mid-large-cap-index": "MLCX",
    # "small-cap-index": "SMLL",
    # "valor-bm-fbovespa": "IVBX",
    # "carbon-efficient": "ICO2",
    # "corporate-sustainability": "ISEE",
    # "consumption": "ICON",
    # "electric-power": "IEEX",
    # "financials": "IFNC",
    # "real-estate": "IMOB",
    # "industrial-sector": "INDX",
    # "basic-materials": "IMAT",
    # "public-utilities": "UTIL",
    # "bm-fbovespa-real-estate-ifix": "IFIX",
    # "bm-fbovespa-unsponsored-bdrx": "BDRX",
}


class CrawlerSpider(Spider):
    name = 'Index'
    # Keep this block
    PATH = (os.getcwd())
    PATHS = re.split('\\\\|/', PATH)
    MIC = PATHS[len(PATHS)-1]
    DATE_CRAWL = datetime.now().strftime('%Y-%m-%d')
    LOG_TIME = datetime.now().strftime('%d')
    custom_settings = {
        'LOG_FILE': LOG_PATH + '/logfile/'+MIC+'_'+name+'_'+LOG_TIME+'.log',

        # HUNG ADD
        # 'PLAYWRIGHT_LAUNCH_OPTIONS': {'headless': False},
        'PLAYWRIGHT_ABORT_REQUEST': should_abort_request,
        'PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT': 100000,
        # 'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }
    # End block

    def start_requests(self):
        urls = list(map(fill_quote, list(QUOTES)))
        for url in urls:
            yield Request(url, meta={
                'playwright': True,
                'playwright_include_page': True,
                # 'playwright_context': 'new',
                # 'playwright_context_kwargs': {
                #     'storage_state': COOKIES_FILE,
                # },
                'errback': self.errback,
            },)

    async def parse(self, resp):
        # this shit response only have 1 month historical data!
        symbol = QUOTES.get(ext_quote(resp.url))
        desp = resp.xpath("//h1/text()").get()

        # Now we fuck it and have all historical data that we need
        page = resp.meta["playwright_page"]
        await page.locator(".DatePickerWrapper_icon__Qw9f8").click()
        await page.wait_for_timeout(500)
        # await page.get_by_role("textbox").nth(1).fill("2019-10-24")
        await page.get_by_role("textbox").nth(1).fill("2022-10-24")     # for test
        await page.wait_for_timeout(500)
        await page.get_by_role("button", name="Apply").click()
        await page.wait_for_timeout(3000)
        await page.keyboard.down("End")

        texts = await page.locator("xpath=//table[@data-test='historical-data-table']/tbody/tr").all_inner_texts()
        for text in texts:
            time_, close_, open_, high_, low_, vol_, change_  = text.split("\t")
            yield {
                "Code": symbol,
                "Symbol": symbol,
                "Description": desp,
                "CountryCode": 'BRA',
                "MIC": 'BVMF',
                'Data Source': "https://www.investing.com",
                "Time Enter": self.DATE_CRAWL,
                "Iso currency code": 'BRL',
                "Date": get_time(time_),
                "Close": get_number(close_),
                "Open": get_number(open_),
                "High": get_number(high_),
                "Low": get_number(low_),
                "Volume": get_vol(vol_),
                "Change": change_,
            }

        await page.wait_for_timeout(500)
        await page.close()

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
