import requests
import json

base_url = 'https://reqres.in'
url = f'{base_url}/api/login'

payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

response = requests.post(url, data=payload)
print(response.text)
token = json.loads(response.text)['token']
print("================================================")


url = 'https://reqres.in/api/users/'

headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get(url, headers=headers)


json_data = response.text
data = json.loads(json_data)
data = json.dumps(data, indent=4)
print(data)
print(response.request.headers)
