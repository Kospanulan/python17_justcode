
s = 'hello world from justcode'
# s = 'hello'

result = {}

for char in s:
    if char not in result.keys():
        result[char] = 1
    else:
        result[char] = result[char] + 1

print(result)










