
data = {
    "student1": ['pred1', 'pred2', 'pred3'],
    "student2": ['pred1', 'pred2'],
    "student3": ['pred1', 'pred2', 'pred1', 'pred2'],
}

result = {}
for key, value in data.items():
    # print(f"{key}: {len(value)}")
    result[key] = len(value)

m = max(result.values())

for key, value in result.items():
    if value == m:
        print(key)


