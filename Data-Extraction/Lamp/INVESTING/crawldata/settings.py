BOT_NAME = 'crawldata'
SPIDER_MODULES = ['crawldata.spiders']
NEWSPIDER_MODULE = 'crawldata.spiders'

# # pip install scrapy-rotating-proxies
# ROTATING_PROXY_LIST_PATH = '/home/proxies.txt'
# ROTATING_PROXY_PAGE_RETRY_TIMES=100

URLLENGTH_LIMIT = 50000
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOW_ALL = True

#CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 0.3
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'content-type': 'text/plain',
    'Connection': 'keep-alive',
    'TE': 'trailers',
}

# # Un lock this block if use proxies
# DOWNLOADER_MIDDLEWARES = {
#    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
# }

# ITEM_PIPELINES = {
#     'crawldata.pipelines.CrawldataPipeline': 300,
# }

LOG_ENABLED = True
LOG_LEVEL = 'ERROR'
LOG_FORMAT = '%(levelname)s: %(message)s'

# Set path to store log file in the log_path.txt file
LOG_PATH = open('../log_path.txt', 'r', encoding='utf-8').read()
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'