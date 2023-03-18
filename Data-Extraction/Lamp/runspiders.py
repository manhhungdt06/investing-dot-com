# Run on every 30 minutes
import os
from datetime import datetime
import json


def dumpthing(num: int = None) -> int:
    if num < 15:
        num = 14
    elif num < 30:
        num = 29
    elif num < 45:
        num = 44
    else:
        num = 59
    return num


PRJ_FOLDER = "PRICE"
USE_PROD = False    # switch bwtween Prod and HN Crawler Server
SCRAPY_ROOT = "/root/anaconda3/bin/scrapy" if USE_PROD else "/home/wvbadmin/anaconda3/bin/scrapy"
# '''
# Hung refactor
now = datetime.utcnow()
print("RUN TIME: UTC Time ", now.strftime("%Y-%m-%d %a-%H:%M"))
CURRENT_DATE, CURRENT_HOUR, CURRENT_MINUTE = now.strftime(
    "%a"), now.hour, now.minute
# Hung refactor
# '''
HOUR_ADD, MINUTE_ADD = 0, 0
RUN_HOUR, RUN_MINUTE = CURRENT_HOUR+HOUR_ADD, CURRENT_MINUTE+MINUTE_ADD

# unknow LOGIC
if RUN_MINUTE >= 60:
    RUN_MINUTE, RUN_HOUR = RUN_MINUTE-60, RUN_HOUR+1
RUN_MINUTE = dumpthing(RUN_MINUTE)
RUN_HOUR = RUN_HOUR-24 if RUN_HOUR >= 24 else RUN_HOUR
# unknow LOGIC

Root = os.getcwd()
with open(f"{Root}/runtime.json") as f:
    LIST = json.load(f)
for row in LIST:
    mic, rtime, holiday, spiders = row.values()   # true order
    if holiday and CURRENT_DATE.lower() in holiday.lower():  # check holiday can't be empty
        pass
    else:
        HOUR, MINUTE = int(rtime.split(":")[0]), int(rtime.split(":")[1])
        if HOUR == RUN_HOUR:
            MINUTE = dumpthing(MINUTE)
            if RUN_MINUTE == MINUTE:
                sp = spiders.split(",")     # supose sp are not empty
                for rs in sp:
                    FILENAME = f"{mic}_{rs}_{now.strftime('%Y-%m-%d')}"     # ??? not using
                    COMMAND = f"cd {Root}/{PRJ_FOLDER}/{mic} && {SCRAPY_ROOT} crawl {rs} --nolog"
                    os.system(COMMAND)
