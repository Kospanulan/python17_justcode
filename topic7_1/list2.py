
a = ['Hello', 23, 'World', 45]
print(f"old a: {a}")

# a.remove(23)


# elem = a[2]
# print(f"elem: {elem}")
# print("Поработали с elem...")
# a.pop(2)
# print("И удалили его...")

popped_elem = a.pop(2)
print(f"Удалили elem: {popped_elem}")
print("Поработали с elem...")

print(f"new a: {a}")

