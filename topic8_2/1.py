
def get_square(x):
    return x*x


def get_sum_of_squares(a, b, our_custom_func):
    # return a*a + b*b
    return our_custom_func(a) + our_custom_func(b)


# print(get_square(8))
# print(get_square)
print(get_sum_of_squares(2, 4, get_square))





