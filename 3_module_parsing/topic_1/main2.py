import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(
    markup=response.text,
    features="html.parser"
)

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tag_groups = soup.find_all('div', class_='tags')

for i in range(len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    print("--------------------------------\n")

    print(tag_groups[i])
    print(type(tag_groups[i]))
    print("--------------------------------\n")
    tags = tag_groups[i].find_all('a')

    for tag in tags:
        print(tag.text)

    print("================================\n")

