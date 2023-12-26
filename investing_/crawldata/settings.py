from crawldata.functions import random_user_agent

BOT_NAME = 'crawldata'
SPIDER_MODULES = (
    'crawldata.spiders',
    'crawldata.spiders.babypips',
    'crawldata.spiders.barchart',
    'crawldata.spiders.cme',
    'crawldata.spiders.dailyfx',
    'crawldata.spiders.finviz',
    'crawldata.spiders.forexfactory',
    'crawldata.spiders.forexsb',
    'crawldata.spiders.fred',
    'crawldata.spiders.fxempire',
    'crawldata.spiders.fxssi',
    'crawldata.spiders.fxstreet',
    'crawldata.spiders.investing',
    'crawldata.spiders.mql5',
    'crawldata.spiders.myfxbook',
    'crawldata.spiders.seekingalpha',
    'crawldata.spiders.tradingeconomics',
)
NEWSPIDER_MODULE = "crawldata.spiders"
USER_AGENT = random_user_agent()
URLLENGTH_LIMIT = 50000
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOW_ALL = True
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
TELNETCONSOLE_ENABLED = False

LOG_ENABLED = True
LOG_LEVEL = 'ERROR'
LOG_FORMAT = '%(levelname)s: %(message)s'

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

# CONCURRENT_REQUESTS = 32
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# # Un lock this block if use proxies
# ROTATING_PROXY_LIST_PATH = '/home/hung/proxies.txt'
# ROTATING_PROXY_PAGE_RETRY_TIMES=100
# DOWNLOADER_MIDDLEWARES = {
#    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
# }
# CONCURRENT_REQUESTS_PER_IP = 1
# ITEM_PIPELINES = {'crawldata.pipelines.CrawldataPipeline': 300,}