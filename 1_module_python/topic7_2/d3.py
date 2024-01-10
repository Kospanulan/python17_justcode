
# s = 'hello world from justcode'
s = 'hello'

result = {
    'h': 0,
    'e': 0,
    'l': 0,
    'o': 0,
}

for char in s:
    print(f"char: {char}")
    print(f"old result[char]: {result[char]}")
    result[char] = result[char] + 1
    print(f"new result[char]: {result[char]}\n")


print(result)



