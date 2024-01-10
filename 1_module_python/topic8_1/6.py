# args - arguments

def sum_of_n(*args):
    result = 0
    for num in args:
        result = result + num

    return result


res = sum_of_n(12, 8, 40, 89)
print(f"result: {res}")


