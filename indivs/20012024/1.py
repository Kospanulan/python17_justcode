
def get_kub(x):
    return x*x*x


def get_square(x):
    return x*x


def sum_of_x(a, b, my_func):
    # return get_square(a) + get_square(b)
    return my_func(a) + my_func(b)


print(get_square)
print(get_square(2))

res = sum_of_x(2, 5, get_square)
res2 = sum_of_x(2, 2, get_kub)

print(res)
print(res2)


# def func(a):
#   ...

# func(12)

# func
