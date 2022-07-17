import requests
import json

base_url = "https://api.hypixel.net/skyblock/auctions_ended"

r = requests.get(base_url)

data = r.json()

print(data["auction_id"])