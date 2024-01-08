# Найти сумму всех четных чисел до N

n = int(input('n = '))

number = 0
result = 0
# % - остаток от деления

while number < n:
    number = number + 1

    if number % 2 == 0:
        print(number)
        result = result + number

print(f"Результат: {result}")
