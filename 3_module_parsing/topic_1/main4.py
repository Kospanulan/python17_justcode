import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(response.headers)


soup = BeautifulSoup(
    markup=response.text,
    features="html.parser"
)

full_quotes = soup.find_all('div', class_='quote')

for full_quote in full_quotes:
    quote = full_quote.find('span', class_='text')
    author = full_quote.find('small', class_='author')
    tags = full_quote.find_all('a', class_='tag')

    print(quote.text)
    print(author.text)

    tag_texts = [tag.text for tag in tags]
    print(", ".join(tag_texts))
    print("\n================================\n")
