from public_functions import *
from crawldata.items import PricingItem, IndexItem
# import cx_Oracle
import json
import sys
import os
from crawldata.settings import LOG_PATH
sys.path.append(os.path.abspath("../"))


class CrawldataPipeline:
    def open_spider(self, spider):
        # jsonfile = '../connection/price_connect.json'
        # strconn = open(jsonfile, 'r', encoding='utf-8')
        # account = json.load(strconn)
        # spider.conn = None
        # for row in account:
        #     if not spider.conn:
        #         try:
        #             # spider.conn = cx_Oracle.connect(
        #             #     str(row['CONNECT']), encoding="UTF-8", nencoding="UTF-8")
        #             print(row['NAME'])
        #         except:
        #             print("CAN NOT", row['NAME'])
        #             pass
        pass

    def close_spider(self, spider):
        # log_file = LOG_PATH+'/summary/'+spider.MIC + \
        #     '_'+spider.name+'_'+spider.LOG_TIME+'.json'
        # SUMMARY = spider.crawler.stats.get_stats()
        # SUMMARY['start_time'] = SUMMARY['start_time'].strftime(
        #     '%Y-%m-%dT%H-%M-%S')
        # f = open(log_file, 'w', encoding='utf-8')
        # f.write(json.dumps(SUMMARY))
        # f.close()
        # if spider.conn:
        #     spider.conn.close()
        pass

    def process_item(self, item, spider):
        # if isinstance(item, PricingItem):
        #     if (item['CLOSE_PRICE'] != "") and item['CLOSE_PRICE'] != "None" and float(item['CLOSE_PRICE']) > 0:
        #         #print("Do with Price function")
        #         KQ = Do_PRICE(item, spider.conn)
        #     pass
        # elif isinstance(item, IndexItem):
        #     if item['CLOSE_VALUE'] != "" and item['CLOSE_VALUE'] != "None" and float(item['CLOSE_VALUE']) > 0:
        #         #print("Do with Index function")
        #         KQ = Do_INDEX(item, spider.conn)
        #     pass
        # return item
        pass
