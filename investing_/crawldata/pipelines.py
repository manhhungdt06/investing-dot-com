from crawldata.functions import *
from crawldata.items import *


class CrawldataPipeline:
    def open_spider(self, spider):
        self.client = connect_db(is_local=True)
        db, collection = spider.name.split('_')
        print(db, collection)
        self.collection = self.client[db][collection]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        filters = dict()
        # match item:
        #     # case CalendarItem():
        #     #     filters = {'time_': item.get('time_'),}
        #     # case MarketItem():
        #     #     filters = {'type_': item.get('type_'), 'quote_': item.get('quote_'), 'period_': item.get('period_'), 'window_': item.get('window_')}
        #     case NewsItem():
        #         filters = {'day_': item.get('day_'), 'type_': item.get('type_')}
        #     case _:
        #         self.logger.error(f"Dont know item type: {type(item)}")
        #         self.client.close()
        #         raise CloseSpider()

        if isinstance(item, PivotsItem):
            filters = {'day_': item.get('day_'), 'type_': item.get('type_'), 'period_': item.get('period_')}
        handle_item(self.collection, item, filters)
        return item