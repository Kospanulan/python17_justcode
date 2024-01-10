
def custom_filter(my_func, my_list):
    res = []
    for elem in my_list:
        if my_func(elem):
            res.append(elem)
    return res


numbers = [2, 45, 56, 13, 99, 5]

odd_numbers = custom_filter(lambda x: x % 2 != 0, numbers)
print(odd_numbers)
