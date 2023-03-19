# Keep those libs
import scrapy
import os
import re
import json
from datetime import datetime
from crawldata.items import IndexItem
from crawldata.settings import LOG_PATH
# End libs
from datetime import date, timedelta
from crawldata.functions import *
from pathlib import Path
current_folder = Path(__file__).parent.resolve()

class CrawlerSpider(scrapy.Spider):
    name = 'Index'
    # Keep this block
    PATH = (os.getcwd())
    PATHS = re.split('\\\\|/', PATH)
    MIC = PATHS[len(PATHS)-1]
    DATE_CRAWL = datetime.now().strftime('%Y-%m-%d')
    LOG_TIME = datetime.now().strftime('%d')
    custom_settings = {'LOG_FILE': LOG_PATH + '/logfile/'+MIC+'_'+name+'_'+LOG_TIME+'.log'}
    # End block

    def start_requests(self):
        url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Language': 'en-GB,en;q=0.5',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Connection': 'keep-alive', }

        # start_date = date.today()
        start_date = date.today() - timedelta(1)
        end_date = date.today() - timedelta(90)
        # end_date = date(2022, 6, 30)

        while start_date != end_date:
            if start_date.isoweekday() not in (6, 7):
                # index have 1-4 filter page: KRX~1, KOSPI~2, KOSDAQ~3, 테마~4
                day = start_date.strftime('%Y%m%d')
                for page_idx in range(1, 5):
                    data = f'bld=dbms/MDC/STAT/standard/MDCSTAT00101&locale=en&idxIndMidclssCd=0{page_idx}&trdDd={day}&share=2&money=3&csvxls_isNo=false'
                    yield scrapy.Request(url=url, callback=self.parse,
                                         body=data, headers=headers,
                                         method="POST", meta={'dl_day': start_date.strftime('%Y-%m-%d')})
            start_date -= timedelta(1)

    def parse(self, response):
        data = json.loads(response.text)
        if data.get('output'):
            for price in data.get('output'):
                item = IndexItem()
                CODE = price.get("IDX_NM")
                item['INDEX_PERM_ID'] = ""
                item['INDEX_CODE'] = get_code(CODE)
                item['INDEX_SYMBOL'] = price.get("INDEX_CODE")
                item['INDEX_DESC'] = CODE
                item['ACTIVE_INACTIVE_FLAG'] = "A"
                item['ISO_COUNTRY_CODE'] = "KOR"
                item['INDEX_MIC'] = "XKRX"
                item['DATA_SOURCE'] = "http://data.krx.co.kr"
                item['DTIME_ENTERED'] = self.DATE_CRAWL
                item['WHERE_ENTERED'] = "HN"
                item['WHO_ENTERED'] = "HUNG"
                item['ISO_CURRENCY_CODE'] = "KRW"
                item['INDEX_DATE'] = response.meta['dl_day']
                item['OPEN_VALUE'] = get_number(price.get("OPNPRC_IDX"))
                item['CLOSE_VALUE'] = get_number(price.get("CLSPRC_IDX"))
                item['DAILY_HIGH'] = get_number(price.get("HGPRC_IDX"))
                item['DAILY_LOW'] = get_number(price.get("LWPRC_IDX"))
                item['VOLUME'] = get_number(price.get("ACC_TRDVOL"))
                item['VALUE_LOCAL_CURRENCY'] = get_number(
                    price.get("ACC_TRDVAL"))
                item['HANDLING_CODE'] = "2"
                item['SESS_ID'] = "0"
                yield (item)
