# args - arguments
# kwargs - keyword arguments

def sum_of_n(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


sum_of_n(x=12, b=8, c=40, d=89)
# res = sum_of_n(12, 8, 40, 89)
# print(f"result: {res}")
