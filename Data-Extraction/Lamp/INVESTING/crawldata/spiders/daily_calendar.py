# Keep those libs
import scrapy
import os
import re
from datetime import datetime, timezone
from crawldata.items import AnalysisItem
from crawldata.settings import LOG_PATH
# End libs
from crawldata.functions import *
import pandas as pd


class CrawlerSpider(scrapy.Spider):
    name = 'ecocalendar'

    # Keep this block
    PATHS = re.split('\\\\|/', os.getcwd())
    MIC = PATHS[len(PATHS)-1]
    DATE_CRAWL = datetime.now().strftime('%Y-%m-%d')
    LOG_TIME = datetime.now().strftime('%d')
    custom_settings = {'LOG_FILE': LOG_PATH +
                       '/logfile/'+MIC+'_'+name+'_'+LOG_TIME+'.log'}
    # End block

    start_urls = [
        'https://www.dailyfx.com/economic-calendar'
    ]

    def parse(self, resp):
        # filtering after
        for it in resp.xpath("//tr[contains(@class, 'economicCalendarRow')]"):
            pass

        #     time_ = it.xpath("normalize-space(./h2/text())").get()
        #     url = it.xpath("./a/@href").get()
        #     title = it.xpath("./a/text()").get()
        #     scontent = it.xpath("normalize-space(./p/text())").get()
        #     tf = it.xpath("./div/div[2]/span[2]/text()").get()
        #     expertise = it.xpath("./div/div[3]/span[2]/text()").get()
        #     data = (status, title, scontent, tf, expertise)
        #     yield scrapy.Request(url, callback=self.parse_detail, meta={'data': data})
        pass

    # def parse_detail(self, resp):
    #     status, title, scontent, tf, expertise = resp.meta['data']
    #     time_ = resp.xpath("//time/@datetime").get()
    #     temp = list()
    #     main_term = resp.xpath("(//article/ul)[1]")
    #     if main_term:
    #         for it in main_term.xpath("./li"):
    #             temp.append(''.join(it.xpath("./descendant-or-self::*/text()").getall()))

    #     item = AnalysisItem()
    #     item['status'] = status
    #     item['timeframe'] = tf
    #     item['expertise'] = expertise
    #     item['title'] = title
    #     item['time'] = time_
    #     item['scontent'] = scontent
    #     item['mainterm'] = temp
    #     yield item
 