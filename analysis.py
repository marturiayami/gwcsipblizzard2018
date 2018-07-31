import json
with open("data.json", "r+") as f:
    old_data = json.load(f)

for response in old_data.items():
    print(response)
