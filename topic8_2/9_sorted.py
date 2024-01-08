# ./! 0-9 A-Z a-z

numbers = [2, 45, 56, 13, 99, 5]
# key   =  -2, -45, -56, -13, -99, -5

# result = sorted(numbers, key=lambda x: -x)
result = sorted(numbers, reverse=True)

# words = ["hi", "justcode", "world", "Hello", "apple"]
# key =   2,      7,          5,       5,       5
# key_res = 2, 5, 5, 5, 7

# result = sorted(words, key=lambda x: x)
# result = sorted(words, key=lambda x: len(x))

d = {
    "a": 12,
    "er": 99,
    "b": 8
}

# result = sorted(d.items(), key=lambda x: x[1], reverse=True)

print(result)
