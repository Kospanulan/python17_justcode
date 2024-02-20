import requests
from bs4 import BeautifulSoup

url = "https://2ip.ru/"

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, "html.parser")

link_elements = soup.find_all(name="a", attrs={"href": lambda x: x.startswith("https://2ip.ru/isp")})

print(link_elements)
