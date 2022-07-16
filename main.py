import requests
import json

response_API = requests.get("https://api.hypixel.net/skyblock/auctions_ended") # můžeš zkusit ještě 'https://api.hypixel.net/skyblock/auctions'
data = response_API.text # Nejsem si jistý, ale myslím, že .content by bylo lepší, mělo by ti to vrátit přímo JSON formát a nemusel by jsi dělat json.loads(), ale nejsem si tímhle úplně jistý
parse_json = json.loads(data)
auction_details = parse_json["auctions"]  #auction_details = json.loads(response_API.text)['auctions'] můžeš to udělat jen takhle (čitelnější code, méně řádku)
print(auction_details)
