import requests
import json

response_API = requests.get("https://api.hypixel.net/skyblock/auctions_ended")
data = response_API.text
parse_json = json.loads(data)
auction_details = parse_json["auctions"]
print(auction_details)
