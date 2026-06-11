import sys
import requests
import json


if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search",
    params={"entity": "song", "limit": 1, "term": sys.argv[1]},
    timeout=10,
)

print(json.dumps(response.json()))