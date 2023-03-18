# Keep those libs
import scrapy
import os
import re
from datetime import datetime, timezone
from crawldata.items import NewsItem
from crawldata.settings import LOG_PATH
# End libs


def beau_time(string: str = None) -> str:
    if string:
        return datetime.fromisoformat(string).astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    else:
        return None


class CrawlerSpider(scrapy.Spider):
    name = 'news'
    # Keep this block
    PATHS = re.split('\\\\|/', os.getcwd())
    MIC = PATHS[len(PATHS)-1]
    DATE_CRAWL = datetime.now().strftime('%Y-%m-%d')
    LOG_TIME = datetime.now().strftime('%d')
    custom_settings = {'LOG_FILE': LOG_PATH +
                       '/logfile/'+MIC+'_'+name+'_'+LOG_TIME+'.log'}
    # End block

    start_urls = [
        'http://www.dailyfx.com/market-news/articles',
        'https://www.dailyfx.com/technical-analysis/articles',
    ]

    def parse(self, resp):
        for it in resp.xpath("//div[@class='dfx-articleList jsdfx-articleList  ']/a"):
            title = it.xpath("normalize-space(./div/span/text())").get()
            time = beau_time(it.xpath("./div/div[1]/span/@data-time").get())
            scontent = it.xpath("normalize-space(./div/div[2]/text())").get()
            url = it.xpath('./@href').get()

            yield scrapy.Request(url, callback=self.parse_detail,
                                 meta={'data': (title, time, scontent)})

        n_url = resp.xpath("//a[@class='dfx-paginator__link  ms-auto']/@href").get()
        if n_url is not None:
            yield scrapy.Request(resp.urljoin(n_url), callback=self.parse)

    def parse_detail(self, resp):
        title, time, scontent = resp.meta['data']
        temp = list()

        main_term = resp.xpath("(//article/ul)[1]")
        if main_term:
            for it in main_term.xpath("./li"):
                temp.append(
                    ''.join(it.xpath("./descendant-or-self::*/text()").getall()))

        item = NewsItem()
        item['title'] = title
        item['time'] = time
        item['scontent'] = scontent
        item['mainterm'] = temp
        yield item
