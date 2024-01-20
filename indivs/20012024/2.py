
def sum_of_x(a, b, my_func):
    # return get_square(a) + get_square(b)
    return my_func(a) + my_func(b)


res = sum_of_x(2, 5, lambda x: x*x)
res2 = sum_of_x(2, 2, lambda x: x*x*x)
# map, sorted, filter
print(res)
print(res2)

