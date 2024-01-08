

s = 'hello world from justcode'

a = ['a', 'e', 'u', 'o']

# result = []
# for char in s:
#     if char in a and char not in result:
#         result.append(char)

result = set()
for char in s:
    if char in a:
        result.add(char)

print(result)


