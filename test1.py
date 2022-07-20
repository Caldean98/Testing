import requests

response = requests.get("https://api.hypixel.net/skyblock/auctions_ended")

print(response.status_code)
if response.status_code == 200:
    pass
else:
    print("Server je down nebo je něco špatně")

data = response.json()
print(type(data))

data_specification = data["auctions"]

for seller in data_specification:
    print(data.get["seller"])

# print(data.keys())
# print(data.values())
