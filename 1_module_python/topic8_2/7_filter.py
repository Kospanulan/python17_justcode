numbers = [2, 45, 56, 13, 99, 5]


odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(f"odd numbers: {odd_numbers}")
