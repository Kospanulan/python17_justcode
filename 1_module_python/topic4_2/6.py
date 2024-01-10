

a = input("a = ")
result = ""
for char in a:
    if char == ' ':
        continue

    result = result + char


print(f"result = {result}")
