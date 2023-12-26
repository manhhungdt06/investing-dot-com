from scrapy import Item, Field


class NewsItem(Item):
    day_ = Field()
    type_ = Field()
    data_ = Field()


class CalendarItem(Item):
    time_ = Field()
    data_ = Field()


class MarketItem(Item):
    type_ = Field()
    quote_ = Field()
    period_ = Field()
    window_ = Field()
    data_ = Field()


class PivotsItem(Item):
    day_ = Field()
    type_ = Field()
    period_ = Field()
    data_ = Field()


class BarchartQuotes(Item):
    symbols_ = Field()
    filter_ = Field()
    data_ = Field()