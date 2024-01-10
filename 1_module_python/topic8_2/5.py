# squares = [number * number for number in range(5)]
# squares = [number * number for number in numbers]

def get_square(x):
    return x*x


numbers = [2, 45, 56, 13, 99, 5]

# squares = []
# for number in numbers:
#     squares.append(number * number)

# squares = [lambda number: number * number for number in numbers]
squares = [get_square(number) for number in numbers]

print(squares)

