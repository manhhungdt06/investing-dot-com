import os
import json

Root = os.getcwd()
with open(f"{Root}/runtime.json") as f:
    LIST = json.load(f)
for row in LIST:
    mic, time, hol, spider = row.values()
    print(mic, time, hol, spider)