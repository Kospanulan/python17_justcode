num = 1
result = 0

while num <= 5:
    result = result + num          # 0 + 1 | 1 + 2 | 3 + 3 | 6 + 4 | 10 + 5
    print(f"number: {num}")        # 1     | 2     | 3     | 4     | 5
    print(f"result: {result}\n")   # 1     | 3     | 6     | 10    | 15
    num = num + 1

print(f"Конец цикла! result = {result}")
