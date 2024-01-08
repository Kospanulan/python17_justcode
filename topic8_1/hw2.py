
def custom_max(numbers):
    current_max = numbers[0]
    for number in numbers:
        # print(f'current_max: {current_max}\ncurrent num: {number}')
        if number > current_max:
            current_max = number
            # print('меняем!\n')
        else:
            # print('не меняем!\n')
            continue

    return current_max


numbers = [101, 2, 45, 56, 13, 99, 5]

result = custom_max(numbers)
print(f"result: {result}")

