
n = 1

while n <= 5:
    print("Начало итерации...")
    if n == 3:
        print("Используем континью\n")
        n = n + 1
        continue
    print(n)
    n = n + 1
    print("Конец итерации...\n")

print("Цикл завершен!")


