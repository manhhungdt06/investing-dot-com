# -*- coding: utf-8 -*-
import scrapy


class NewsItem(scrapy.Item):
    # Market News Articles
    title = scrapy.Field()
    time = scrapy.Field()
    scontent = scrapy.Field()
    mainterm = scrapy.Field()


class AnalysisItem(scrapy.Item):
    status = scrapy.Field()
    timeframe = scrapy.Field()
    expertise = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    scontent = scrapy.Field()
    mainterm = scrapy.Field()


class CurrenciesItem(scrapy.Item):
    pass


class CommoditiesItem(scrapy.Item):
    pass


class CommoditiesItem(scrapy.Item):
    pass


class CryptoItem(scrapy.Item):
    pass


class CalendarItem(scrapy.Item):
    pass


# ...
