# Дано число двузначное число a, поменять местам цифры используя операторы (%, //). Ожидаемый
# результат: если a = 42, result = 24.

a = 24
first_digit = a // 10
second_digit = a % 10

result = first_digit * 10 + second_digit
print(f"result = {result}")

# print(f"first_digit = {first_digit}")
# print(f"second_digit = {second_digit}")
# print(f"result = {first_digit}{second_digit}")
# print(str(first_digit) + str(second_digit))

