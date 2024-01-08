# args - arguments
# kwargs - keyword arguments

# def sum_of_n(*args, **kwargs):
#
#     print(f"args: {args}")
#     print(f"kwargs: {kwargs}")
#
# sum_of_n(12, 34, 65, 90, a=12, b=8)


def sum_of_n(a, b, *args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    print(f"a: {a}")
    print(f"b: {b}")


sum_of_n(12, 34, 65, 90, k=12, c=65)





