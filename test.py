import requests
import json

BASEURL = "http://127.0.1:8000/"
ENDPOINT = "api/"

url = (BASEURL + ENDPOINT)
response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
