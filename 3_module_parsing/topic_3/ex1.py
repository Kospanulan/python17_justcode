import requests
import json

url = 'https://reqres.in/api/users/'

response = requests.get(url)
json_data = response.text

print(type(json_data))
print(json_data)
print("================================================")

data = json.loads(json_data)
print(type(data))
print(data)
print(data["data"])

"""

from bs4 import BeautifulSoup

url = "https://reqres.in/"
response = requests.get(url)

soup = BeautifulSoup(
    markup=response.text,
    features="html.parser"
)

# print(response.status_code)
# print(response.text)

data = soup.find('h2', class_='tagline')
print(data)
"""
