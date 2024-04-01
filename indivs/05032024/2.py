
# def get_square(x):
#     return x * x
#
# def get_kub(x):
#     return x * x * x


def get_sum(a, b, func):
    return func(a) + func(b)


print(get_sum(1, 5, lambda x: x * x))
print(get_sum(1, 5, lambda x: x * x * x))

# print(get_sum(1, 5, get_square))
# print(get_sum(1, 5, get_kub))
