import requests
from bs4 import BeautifulSoup

url = "https://2ip.ru/"

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, "html.parser")

link_elements = soup.find_all(name="a", attrs={"href": True})

# print(f"Link elements: \n{link_elements}")
print(type(link_elements[6]))
print("================================================")

print(link_elements[6])
print("================================================")

print(link_elements[6].get("href"))
print(link_elements[6]["href"])
print(link_elements[6].attrs)
print("================================================")


next_url = link_elements[6]["href"]
response = requests.get(next_url)
