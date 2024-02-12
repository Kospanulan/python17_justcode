

# a = ["hello", "justcode", "python17", "world"]
# options = ['a', 'b', 'c', 'd']

# for i, word in enumerate(a):
#     print(f"{options[i]}. {word}")

# =================================================================

a = ["hello", "justcode", "python17", "world"]


def func(*args):
    print(args, '\n\n')
    for i in args:
        print(i)


def func2(a, b, c, d):
    print(a, b, c, d)


# func(*a)
func2(*a)




