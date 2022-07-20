import requests
import json

base_url = 'https://api.hypixel.net/skyblock/auctions_ended'

r = requests.get(base_url)

data = r.json()

json_obj = json.load(r)

array = []
for i in json_obj['auction_id']:
    array[i] = i['auction_id']
print(array)


#auctions_all = (data["auctions"])

#print(auctions_all)

