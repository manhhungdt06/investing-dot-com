from ast import literal_eval
from boltons.iterutils import remap
from calendar import monthrange
from configparser import ConfigParser
from datetime import datetime, timezone, timedelta, date
from dateparser import parse
from dateutil import parser
from dateutil.relativedelta import relativedelta
from fake_useragent import VERSION, UserAgent
from json import dump, dumps, load, loads
from pathlib import Path
from pydantic.v1.utils import deep_update
from pymongo import MongoClient
from unicodedata import normalize
from urllib.parse import urlencode, quote_plus
from itertools import product
from random import randint
from re import sub, findall, search, compile, split
# from redis import from_url
from requests import get, post, Session
from scrapy import Spider, Request, FormRequest
from scrapy.exceptions import CloseSpider
from scrapy.http import JsonRequest
from scrapy.selector import Selector
from sys import path


CURRENT_PATH = Path(__file__).resolve().parent
SITE = CURRENT_PATH.parent
# PROJECT = SITE.parent
NOW = datetime.now()
UNIXTIME = str(datetime.timestamp(NOW)*1000).split('.')[0]
CRAWL_DATE = NOW.strftime('%Y-%m-%d')
LOG_TIME = NOW.strftime('%d%m%Y')
IGNORES = ['google',]


# =========================================== COMMONS ============================================
def load_info(filepath=f"{CURRENT_PATH}/_login-tasks/accounts/mongo.ini", user="OBJECTROCKET") -> dict:
    config = ConfigParser()
    config.read(filepath)
    try:
        return config[user]
    except:
        print("User not found!")
        exit(0)


def connect_db(is_local: bool = False):
    if is_local:
        return MongoClient('mongodb://127.0.0.1:27017')
    else:
        config_data = load_info()
        settings = {
            'host': 'lon5-c15-1.mongo.objectrocket.com:43848,lon5-c15-2.mongo.objectrocket.com:43848,lon5-c15-0.mongo.objectrocket.com:43848',
            'username': quote_plus(config_data['username']),
            'password': quote_plus(config_data['password']),
            'options': f"?authSource={config_data['db']}&replicaSet=e58c7b5541b04b3bb6c0dbfa399c5f80".format(**locals())
        }
        try:
            mongodb_uri = "mongodb://{username}:{password}@{host}/{options}"
            return MongoClient(mongodb_uri.format(**settings))
        except Exception as ex:
            print("Error: {}".format(ex))
            exit('Failed to connect, terminating.')


def handle_item(collection, item, filters):
    '''shitty code'''
    documents = collection.find_one(filters)
    if documents:
        new_data = None
        if isinstance(documents.get('data_'), list):
            # add new data to old data
            new_data = item.get('data_') + documents.get('data_')
            new_data = [dict(t) for t in {tuple(d.items()) for d in new_data}]

            # modify dict item of a list: t.b.d
        else:
            new_data = {**documents.get('data_'), **item.get('data_')}
        collection.update_one({'_id': documents.get('_id')}, {
                              '$set': {'data_': new_data}})
    else:
        collection.insert_one(dict(item))


def random_user_agent():
    # VERSION==1.1.3
    ua_loc = f'{CURRENT_PATH}/fake_useragent{VERSION}.json'
    ua = UserAgent(use_external_data=True, cache_path=ua_loc)
    # ua = UserAgent(min_percentage=1.3)
    return ua.random


def rand_timeout(min: int = 8, max: int = 13) -> int:
    return 100*randint(min, max)


def get_time(days: str = None, isfuzzy: bool = False, divide: int = 1, have_hour: bool = False) -> str:
    hour = ' %H:%M' if have_hour else ''
    return parser.parse(days, fuzzy=isfuzzy).strftime(f'%Y-%m-%d{hour}') if days else ""


def get_unixtime(timestamp: str = None, divide: int = 1000, have_hour: bool = False) -> str:
    hour = ' %H:%M' if have_hour else ''
    return datetime.fromtimestamp(int(timestamp)/divide).strftime(f'%Y-%m-%d{hour}') if timestamp else ""


def get_unixdt(dt: datetime = None, multiple: int = 1000):
    return str(datetime.timestamp(dt)*multiple).split('.')[0]


def get_tztime(delta: int = 0):
    tz_time = datetime.now(timezone.utc) + timedelta(delta)
    return tz_time.replace(tzinfo=None).isoformat(timespec="seconds") + 'Z'


def check_dirs(folder: str = None):
    if not Path(folder).exists():
        Path(folder).mkdir(parents=True, exist_ok=True)


def fill_quote(string: str = None, base: str = 'https://shit/{}') -> str:
    return base.format(string) if string else ""


def get_num(string: str = None,
            filter_: str = r"([^0-9.-])") -> str:
    return sub(filter_, "", str(string).strip()) if string else ""


def checknull(string: str = None) -> str:
    return string if string else ""


def clean_str(string: str = None) -> str:
    return string.replace('“', '').replace('”', '').strip() if string else ""


def clean_lst(lst: list = None) -> list:
    lst = [clean_str(normalize('NFKD', ''.join(item)))
           for item in lst if 'Also read:' not in ''.join(item)]
    return list(filter(None, lst))


def flatten_lst_dct(lst: list = None):
    return {k: v for d in lst for k, v in d.items()}


def sort_dict(dct: dict = None) -> dict:
    return {k: v for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}


def clear_dict(dct: dict = None) -> dict:
    return {k: v for k, v in dct.items() if v}


def lst_to_dict(items: list = None) -> dict:
    # convert list of list to dict
    return {item[0]: item[1] for item in items}


def flatten(l):
    return [item for sublist in l for item in sublist]


def should_abort_request(request):
    IGNORES = (
        'google',
        # 'education',
        'sbcharts',
        'forexpros',
        'ad-score',
        'krxd',
        'doubleclick',
    )
    if any(item in request.url for item in IGNORES):
        return True
    if request.resource_type in ("image", "media", "other"):
        return True
    # if request.resource_type == "script":
    #     return True
    # if request.resource_type == "xhr":    # need
    #     return True
    # if request.resource_type == "stylesheet": # slow
    #     return True
    # if request.method.lower() == 'post':
    #     # logging.log(logging.INFO, f"Ignoring {request.method} {request.url} ")
    #     return True
    return False


def get_chunks(lst: list = None, n: int = 2) -> list:
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def del_dictkeys(dict_: dict = None, keys: set = None):
    '''  https://stackoverflow.com/questions/3405715/elegant-way-to-remove-fields-from-nested-dictionaries '''
    def drop_keys(path, key, value): return key not in keys
    return remap(dict_, visit=drop_keys)


def cvtime_dict(dict_: dict = None, key: str = None, func: object = get_time, hour=False):
    return deep_update(dict_, {key: func(dict_[key], divide=1, have_hour=hour)})


def del_nul_ldict(data: list = None):
    return [{k: v for k, v in item.items() if v} for item in data]


def get_cursor(uri: str = None, db: str = None, collection: str = None):
    client = MongoClient(uri)
    return client[db][collection]


def get_lday(time_: datetime = None):
    return monthrange(time_.year, time_.month)[1]


def transform_time(time_str: str = None, format_: str = '%Y-%m-%d'):
    return datetime.strptime(time_str, '%d/%m/%Y').strftime(format_) if time_str else ""


def gen_productwo(tup_one, tup_two, start=1):
    return {i: item for i, item in enumerate(list(product(tup_one, tup_two)), start=start)}


def connect_sen(lst: list) -> str:
    return ' '.join(clean_lst(lst))
# ========================================== END COMMONS =========================================
