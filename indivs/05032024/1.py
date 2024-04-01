def say_hi(name='Damira', age=0):
    print(f"Hello {name}! I am {age}")


say_hi(age=12)
say_hi('Damira', 2)
say_hi('Roma', 3)



# args = arguments
# kwargs = keyword arguments

def sum_of_n(*args):
    res = 0
    for num in args:
        res += num
    return res


# res = sum_of_n(1, 6, 7, 3, 1)
# print(res)



def my_func(**kwargs):
    print("kwargs type:", type(kwargs))
    print("kwargs:", kwargs)
    return 0


res = my_func(a=1, b=2, c=3, d=4)
print(res)

