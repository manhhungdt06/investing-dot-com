# Run on every 30 minutes
import os
import datetime
import json


utc_datetime = datetime.datetime.utcnow()
UTCTIME=utc_datetime.strftime("%a-%H:%M")
print("RUN TIME: UTC Time ",utc_datetime.strftime("%Y-%m-%d %a-%H:%M"))
CURRENT_DATE=UTCTIME.split("-")[0]
CURRENT_HOUR=int((UTCTIME.split("-")[1]).split(":")[0])
CURRENT_MINUTE=int((UTCTIME.split("-")[1]).split(":")[1])
HOUR_ADD=0
MINUTE_ADD=0
RUN_HOUR=CURRENT_HOUR+HOUR_ADD
RUN_MINUTE=CURRENT_MINUTE+MINUTE_ADD
if RUN_MINUTE>=60:
    RUN_MINUTE=RUN_MINUTE-60
    RUN_HOUR=RUN_HOUR+1
if RUN_MINUTE<15:
    RUN_MINUTE=14
elif RUN_MINUTE<30:
    RUN_MINUTE=29
elif RUN_MINUTE<45:
    RUN_MINUTE=44
else:
    RUN_MINUTE=59
if RUN_HOUR>=24:
    RUN_HOUR=RUN_HOUR-24
Root=os.getcwd()
f=open(Root+"runtime.json","r")
LIST=json.load(f)
for row in LIST:
    if CURRENT_DATE.lower() in row['HOLIDAY'].lower():
        pass
    else:
        HOUR=int(row['UTC_TIME'].split(":")[0])
        MINUTE=int(row['UTC_TIME'].split(":")[1])
        if HOUR==RUN_HOUR:
            if MINUTE<15:
                MINUTE=14
            elif MINUTE<30:
                MINUTE=29
            elif MINUTE<45:
                MINUTE=44
            else:
                MINUTE=59
            if RUN_MINUTE==MINUTE:
                sp=row['SPIDERS'].split(",")
                for rs in sp:
                    FILENAME=row['MIC']+"_"+rs+"_"+str(utc_datetime.strftime("%Y-%m-%d"))
                    #Prod4
                    COMMAND="cd "+Root+"/PRICE/"+row['MIC']+"/pricing/ && /root/anaconda3/bin/scrapy crawl "+rs+" --nolog"
                    #HN
                    #COMMAND="cd "+Root+"/PRICE/"+row['MIC']+"/pricing/ && /home/wvbadmin/anaconda3/bin/scrapy crawl "+rs+" --nolog"
                    #print("Get price from",row['MIC']," run ",rs)
                    #print(COMMAND)
                    os.system(COMMAND)