
def custom_map(my_func, my_list):
    res = []
    for elem in my_list:
        square = my_func(elem)
        res.append(square)
    return res


numbers = [2, 45, 56, 13, 99, 5]

squares = custom_map(lambda x: x*2, numbers)
print(squares)







