import requests
import json

url = 'https://reqres.in/api/users/11'


response = requests.get(url)

json_data = response.text


data = json.loads(json_data)

data_str = json.dumps(data, indent=4)
print(data_str)
print("================================================")
print(response.url)

