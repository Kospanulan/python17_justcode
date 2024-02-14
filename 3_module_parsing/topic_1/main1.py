import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

print(response)
print(type(response.text))
print("\n================================\n")

soup = BeautifulSoup(
    markup=response.text,
    features="html.parser"
)

# print(soup)
# print("\n================================\n")
print(type(soup))

print("\n================================\n")

quotes = soup.find_all('span', class_='text')

for quote in quotes:
    print(quote.text)
    # print(type(quote))
    print("================================\n")

