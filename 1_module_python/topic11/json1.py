import json

file = open('test2.json', 'r')

data = file.read()

print(data)
# '{"key": "value", "apple":  2, "banana":  3}'
print(type(data))

data = json.loads(data)
print('after json.loads()')
print(data)
print(data['apple'])
print(type(data))

file.close()




