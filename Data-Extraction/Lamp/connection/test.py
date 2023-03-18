import json

jsonfile = '../connection/price_connect_hung.json'
with open(jsonfile, encoding='utf-8') as f:
    account = json.load(f)
print(account)