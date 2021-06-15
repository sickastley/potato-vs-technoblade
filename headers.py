import requests 
import json


headers = {
    "accept" : "application/json"
    }
response = requests.get("https://icanhazdadjoke.com/", headers=headers)
json_data = json.loads(response.text)

joke = json_data["joke"]
print(joke)
