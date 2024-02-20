# 0 1 1 2 3 5 8 13 21 34
first = 0
second = 1

print(first)
print(second)

i = 2
n = 10

while i < n:
    new = first + second
    print(new)

    # first = second
    # second = new

    first, second = second, new

    i += 1

