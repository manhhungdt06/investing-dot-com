# -*- coding: utf-8 -*-
import scrapy


class PricingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # CROSS_REF Table
    CROSS_REF_ID = scrapy.Field()
    MIC = scrapy.Field()
    ISIN = scrapy.Field()
    CHK_ISIN = scrapy.Field()
    TICKER = scrapy.Field()
    COMPANY_NAME = scrapy.Field()
    SECURITY_DESC = scrapy.Field()
    DTIME_ENTERED = scrapy.Field()
    WHERE_ENTERED = scrapy.Field()
    WHO_ENTERED = scrapy.Field()
    ACTIVE_INACTIVE_FLAG = scrapy.Field()
    HANDLING_CODE = scrapy.Field()
    UK_CODE = scrapy.Field()
    US_CODE = scrapy.Field()
    LOCAL_CODE = scrapy.Field()
    COMPANY_PERM_ID = scrapy.Field()
    EQUITY_SEC_PERM_ID = scrapy.Field()
    # WVB_STOCK_PRICE Table
    PRICE_ID = scrapy.Field()
    PRICE_DATE = scrapy.Field()
    ISO_CURRENCY_CODE = scrapy.Field()
    OPEN_PRICE = scrapy.Field()
    CLOSE_PRICE = scrapy.Field()
    DAILY_HIGH = scrapy.Field()
    DAILY_LOW = scrapy.Field()
    VOLUME = scrapy.Field()
    VALUE_LOCAL_CURRENCY = scrapy.Field()
    BUY_BID = scrapy.Field()
    SELL_OFFER = scrapy.Field()
    BID_VOLUME = scrapy.Field()
    ASK_VOLUME = scrapy.Field()
    NUMBER_OF_TRADE = scrapy.Field()
    LAST_PRICE = scrapy.Field()
    SHARES_OUTSTANDING = scrapy.Field()
    MARKETCAP = scrapy.Field()


class IndexItem(scrapy.Item):
    # WVB_INDEX_CODES Table
    INDEX_PERM_ID = scrapy.Field()
    INDEX_CODE = scrapy.Field()
    INDEX_SYMBOL = scrapy.Field()
    INDEX_DESC = scrapy.Field()
    ACTIVE_INACTIVE_FLAG = scrapy.Field()
    ISO_COUNTRY_CODE = scrapy.Field()
    INDEX_MIC = scrapy.Field()
    DATA_SOURCE = scrapy.Field()
    DTIME_ENTERED = scrapy.Field()
    WHERE_ENTERED = scrapy.Field()
    WHO_ENTERED = scrapy.Field()
    # WVB_INDEX_WEIGHT Table
    ISO_CURRENCY_CODE = scrapy.Field()
    INDEX_DATE = scrapy.Field()
    OPEN_VALUE = scrapy.Field()
    CLOSE_VALUE = scrapy.Field()
    DAILY_HIGH = scrapy.Field()
    DAILY_LOW = scrapy.Field()
    VOLUME = scrapy.Field()
    VALUE_LOCAL_CURRENCY = scrapy.Field()
    HANDLING_CODE = scrapy.Field()
    SESS_ID = scrapy.Field()
