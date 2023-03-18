# Keep those libs
import scrapy
import os
import re
from datetime import datetime, timezone
from crawldata.items import NewsItem
from crawldata.settings import LOG_PATH
# End libs
from crawldata.functions import *

# gen_url function


def fill_quote(string: str = None) -> str:
    return f"http://www.dailyfx.com/{string}"


def beau_time(string: str = None) -> str:
    if string:
        return datetime.fromisoformat(string).astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    else:
        return None


class CrawlerSpider(scrapy.Spider):
    name = 'sentiment'
    # Keep this block
    PATHS = re.split('\\\\|/', os.getcwd())
    MIC = PATHS[len(PATHS)-1]
    DATE_CRAWL = datetime.now().strftime('%Y-%m-%d')
    LOG_TIME = datetime.now().strftime('%d')
    custom_settings = {'LOG_FILE': LOG_PATH +
                       '/logfile/'+MIC+'_'+name+'_'+LOG_TIME+'.log'}
    # End block

    start_urls = [
        'https://www.dailyfx.com/sentiment-report',
    ]
    
    def parse(self, resp):
        # img = resp.xpath("//h2[@id='summary-table']/following-sibling::a[1]/@href").get()
        data = dict()
        # for it, cur in enumerate(resp.xpath("//table/tbody/tr")): # for test
        #     if it == 2:
        #         break
        for cur in resp.xpath("//table/tbody/tr"):
            symbol = cur.xpath("./td[1]/a/span/text()").get()
            data[symbol] = {
                'url': cur.xpath("./td[1]/a/@href").get(),
                'bias': cur.xpath("./td[2]/span/text()").get(),
                'netlong': getnum(cur.xpath("normalize-space(./td[3]/span/text())").get()),
                'netshort': getnum(cur.xpath("normalize-space(./td[4]/span/text())").get()),
                'daily_lchange': getnum(cur.xpath("normalize-space(./td[5]/p[1]/span[1]/text())").get()),
                'weekly_lchange': getnum(cur.xpath("normalize-space(./td[5]/p[2]/span[1]/text())").get()),
                'daily_schange': getnum(cur.xpath("normalize-space(./td[6]/p[1]/span[1]/text())").get()),
                'weekly_schange': getnum(cur.xpath("normalize-space(./td[6]/p[2]/span[1]/text())").get()),
                'daily_oichange': getnum(cur.xpath("normalize-space(./td[7]/p[1]/span[1]/text())").get()),
                'weekly_oichange': getnum(cur.xpath("normalize-space(./td[7]/p[2]/span[1]/text())").get()),
            }
        # for it, symbol in enumerate(data.keys()): # for test
        #     if it == 2:
        #         break
        for symbol in data.keys():
            child = f"//h2[contains(text(), '{symbol}')]/following-sibling::"
            des = "/descendant-or-self::*/"
            p1 = ''.join(resp.xpath(f"{child}p[1]{des}text()").getall())
            p2 = ''.join(resp.xpath(f"{child}p[2]{des}text()").getall())
            p3 = ''.join(resp.xpath(f"{child}p[3]{des}text()").getall())
            paragraph = [p1.strip(), p2.strip(), p3.strip()]
            data[symbol].update({
                'symbolimage': resp.xpath(f"{child}a[1]/@href").get(),
                'paragraph': paragraph
            })
        yield data

    """ # USE IN ANOTHER PURPOSE
    '''Get all prices in particular period'''
    name = 'sentiment'
    # Keep this block
    PATHS = re.split('\\\\|/', os.getcwd())
    MIC = PATHS[len(PATHS)-1]
    DATE_CRAWL = datetime.now().strftime('%Y-%m-%d')
    LOG_TIME = datetime.now().strftime('%d')
    custom_settings = {'LOG_FILE': LOG_PATH +
                       '/logfile/'+MIC+'_'+name+'_'+LOG_TIME+'.log'}
    # End block

    quotes = (
        'aud-usd', 'eur-usd', 'gbp-usd', 'nzd-usd', 'usd-cad', 'usd-chf', 'usd-jpy',
        'eur-aud', 'eur-cad', 'eur-chf', 'eur-gbp', 'eur-jpy', 'eur-nzd',
        'gbp-aud', 'gbp-cad', 'gbp-chf', 'gbp-jpy', 'gbp-nzd',
        # audxxx, cadxxx, nzdxxx ~ T.B.D
        'gold-price', 'copper-prices', 
    )
    
    start_urls = list(map(fill_quote, quotes))

    def parse(self, resp):
        quote = resp.xpath("//div[@class='dfx-singleInstrument__name']/span/span/text()").get()
        # daily_chg = resp.xpath("//div[contains(@class, 'changeDailyContainer')]/div[3]/div/span[2]/text()").getall()
        # daily_chg = [getnum(strnum) for strnum in daily_chg]

        # weekly_chg = resp.xpath("//div[contains(@class, 'changeWeeklyContainer')]/div[3]/div/span[2]/text()").getall()
        # weekly_chg = [getnum(strnum) for strnum in weekly_chg]

        tempart = list()
        for art in resp.xpath("//div[contains(@class, 'dfx-newsAnalysis')]/div/a"):
            temp = dict()
            temp['title'] = art.xpath("./div/span/text()").get()
            temp['time'] = art.xpath("./div/div/span/@data-time").get()
            temp['url'] = art.xpath("./@href").get()
            tempart.append(temp)

        data = {
            # 'bias' : resp.xpath("normalize-space(//div[@class='dfx-technicalSentimentCard__pairAndSignal']/span[2]/text())").get(),
            'cur_bid': getnum(resp.xpath("//div[contains(@class, 'jsdfx-singleInstrument__priceWrapper')]/div[1]/@data-value").get()),
            'cur_ask': getnum(resp.xpath("//div[contains(@class, 'jsdfx-singleInstrument__priceWrapper')]/div[2]/@data-value").get()),
            'cur_change': getnum(resp.xpath("//div[contains(@class, 'dfx-singleInstrument__change')]/@data-value").get()),
            'cur_high': getnum(resp.xpath("//tr[@class='dfx-lowHighFigures__high']/td[1]/span/@data-value").get()),
            'cur_low': getnum(resp.xpath("//tr[@class='dfx-lowHighFigures__low']/td[1]/span/@data-value").get()),
            'scale': int(resp.xpath("//tr[@class='dfx-lowHighFigures__high']/td[1]/span/@data-unscaling-factor").get()),
            'news': tempart,

            # 'daily_change': daily_chg,
            # 'weekly_change': weekly_chg,
            # 'fore': resp.xpath("(//span[contains(text(), 'IG Client Sentiment:')])[last()]/text()").get(),
            # 'time_for': resp.xpath("(//span[contains(text(), 'IG Client Sentiment:')])[last()]/following-sibling::div/span/@data-time").get(),
        }
        # print(resp.url, quote)

        yield {quote: data}

        # detail_url = resp.xpath("//a[contains(@class, 'dfx-technicalSentimentCard__articleImageWrapper')]/@href").get(),
        # if detail_url:
        #     yield scrapy.Request(detail_url[0], callback=self.parse_detail, meta={'quote': quote, 'data': data})
        # else:
        #     yield {quote: data}
        
    def parse_detail(self, resp):
        '''Not using anymore'''
        quote, data = resp.meta['quote'], resp.meta['data']
        data['time'] = resp.xpath("//div[@class='dfx-articleHead__articleDetails']/time/@data-time").get()
        data['context'] = resp.xpath("(//article)[2]/h2/text()").get()
        data['img'] = resp.xpath("(//article)[2]/a/@href").get()
        # data['netlong'] = getnum(resp.xpath("(//article)[2]/table/tbody/tr/td[3]/span/text()").get())
        # data['netshort'] = getnum(resp.xpath("(//article)[2]/table/tbody/tr/td[4]/span/text()").get())

        paras = list()
        for para in resp.xpath("(//article)[2]/p"):
            temp = ''.join(para.xpath("./descendant-or-self::*/text()").getall())
            paras.append(temp.strip())
        data['paragraph'] = paras

        yield {quote: data}
    
    """
