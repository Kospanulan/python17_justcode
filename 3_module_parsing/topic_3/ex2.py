import requests
import json

url = 'https://reqres.in/api/users/'

payload = {
    'page': 2,
    'per_page': 3
}

response = requests.get(url, params=payload)

json_data = response.text


data = json.loads(json_data)

data_str = json.dumps(data, indent=4)
print(data_str)
print("================================================")
print(response.url)

