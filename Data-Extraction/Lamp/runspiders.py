# Run on every 30 minutes
import os
from datetime import datetime
import json


# '''
# Hung refactor
def dumpthing(num: int = 69) -> int:
    return 14 if num < 15 else 29 if num < 30 else 44 if num < 45 else 59


PRJ_FOLDER = "PRICE"
USE_PROD4 = False    # switch bwtween Prod and HN Crawler Server
SCRAPY_ROOT = "/root/anaconda3/bin/scrapy" if USE_PROD4 else "/home/wvbadmin/anaconda3/bin/scrapy"
now = datetime.utcnow()
print("RUN TIME: UTC Time ", now.strftime("%Y-%m-%d %a-%H:%M"))
CURRENT_DATE, CURRENT_HOUR, CURRENT_MINUTE = now.strftime("%a"), now.hour, now.minute
# Hung refactor
# '''

# unknow LOGIC
HOUR_ADD, MINUTE_ADD = 0, 0
RUN_HOUR, RUN_MINUTE = CURRENT_HOUR+HOUR_ADD, CURRENT_MINUTE+MINUTE_ADD
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
                    # FILENAME = f"{mic}_{rs}_{now.strftime('%Y-%m-%d')}"
                    COMMAND = f"cd {Root}/{PRJ_FOLDER}/{mic} && {SCRAPY_ROOT} crawl {rs} --nolog"
                    os.system(COMMAND)
