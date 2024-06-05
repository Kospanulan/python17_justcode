import json

import requests

# response = requests.get("http://127.0.0.1:8000/posts/1/")
#
# print(response.content)
# print(type(response.content))
#
# post = json.loads(response.content)
#
# print(type(post))
# print(post)

new_post = {
    "title": "Test Title for Post #3",
    "content": "Test content for post #3",
}

response = requests.post(
    url="http://127.0.0.1:8000/posts/",
    json=new_post
)











