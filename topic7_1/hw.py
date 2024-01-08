# O(n)

a = "aafaa"
#    012345
#   -6   -1

is_palindrom = True
for i in range(len(a)//2):
    if a[i] != a[-i-1]:
        is_palindrom = False
        break

if is_palindrom:
    print("Палиндром")
else:
    print("Не палиндром")



# if a == a[::-1]:
#     print("Палиндром")
# else:
#     print("Не палиндром")

