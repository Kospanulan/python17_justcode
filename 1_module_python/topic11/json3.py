import json

data = {
    'apple': 2,
    'name': 'JustCode',
    'age': 20
}


file = open("test3.json", 'w')
json.dump(data, file)

file.close()

