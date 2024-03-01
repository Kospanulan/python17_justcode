import requests
import json


def get_news_from_tengrinews():
    url = 'https://tengrinews.kz'

    response = requests.get(url)
    json_data = response.text

    print(type(json_data))
    print(json_data)
    print("================================================")

    data = json.loads(json_data)
    print(type(data))
    print(data)
    print(data["data"])
