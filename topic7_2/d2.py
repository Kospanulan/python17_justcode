
data = [
    {
        "age": 12,
        "name": "John",
        "email": "john@example.com",
        "phone": "123-456-789"
    },
    {
        "age": 24,
        "name": "James",
        "email": "james@example.com",
        "phone": "345"
    },
    {
        "age": 8,
        "name": "Michael",
        "email": "michael@example.com",
        "phone": "789"
    }
]

a = ["dict1", "dict2", "dict3", "dict4", "dict5"]

for d in data:
    print(d)
    if d['age'] > 10:
        print("Старше 10")

# for elem in d:
#     if elem['age'] < 20:
#         for key, value in elem.items():
#             print(f"{key}: {value}")
#
#     print()

