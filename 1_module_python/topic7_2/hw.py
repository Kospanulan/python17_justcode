
s = 'hello world from justcode, not from ulan.'

words = list(map(lambda word: word.strip('.,'), s.split(' ')))
# words = s.split(' ')
# for i in range(len(words)):
#     words[i] = words[i].strip('.,')

print(f"{words = }")

result = {}

# for word in words:
#     if word in result.keys():
#         result[word] = result[word] + 1
#     else:
#         result[word] = 1

for word in words:
    result[word] = result.get(word, 0) + 1

# print(result.get('ulan', 0))
print(result)

