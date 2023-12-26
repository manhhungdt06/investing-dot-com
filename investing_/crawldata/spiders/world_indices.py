from crawldata.functions import *
from csv import DictReader


class CrawlerSpider(Spider):
    name = 'world_indices'
    custom_settings = {'LOG_FILE': f"{SITE}/log/{name}_{LOG_TIME}.log", }
    start_urls = ('https://www.investing.com/indices/world-indices?majorIndices=on&additionalIndices=on&include-major-indices=true&include-additional-indices=true',)

    def parse(self, response):
        for row in response.xpath("//tr[contains(@id, 'pair_') and not(contains(@id, 'sb_'))]/td[2]"):
            yield response.follow(row.xpath("./a/@href").get(), callback=self.parse_components, headers={'User-Agent': random_user_agent(),}, meta={'data': row.xpath("./span/@data-id").get()})

    def parse_components(self, response):
        yield Request('https://www.investing.com/indices/Service/PriceInstrument?'+urlencode({'pairid': response.meta.get('data'), 'sid': '6ebc4850ebf9379ff40cee9954c189f4', 'filterParams': '', 'smlID': '2032539'}), callback=self.parse_index, headers={'User-Agent': random_user_agent(), 'X-Requested-With': 'XMLHttpRequest'}, meta={'data': get_key(response.xpath("//h1/text()").get())})

    def parse_index(self, response):
        code, name = response.meta.get('data')
        index_ids = response.xpath("//tbody/tr/td[2]/span/@data-id").getall()
        matching = list() 
        with open(f"{SITE}/resources/WW/stocks.csv") as file:
            stock_dict = DictReader(file)
            for item in stock_dict:
                matching.append(item) if item.get('id') in index_ids else None
        yield {'index_name': name, 'index_code': code, 'components': matching}