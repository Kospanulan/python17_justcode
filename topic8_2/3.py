
def get_sum_of_squares(a, b, get_square):
    return get_square(a) + get_square(b)


result = get_sum_of_squares(2, 4, lambda x: x*x)
print(result)



