
def get_max_number(a, b):
    if a > b:
        return a
    else:
        return b


max_number = lambda a, b: a if a > b else b

print(max_number(11, 9))
print(get_max_number(11, 9))
