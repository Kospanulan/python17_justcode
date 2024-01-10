a = "Hello World!"
#    0123456789

# a = ["hello", "Hello", "!mk", "65", "World", "War"]
#       0       1         2     3      4       5
#      -6      -5        -4    -3     -2      -1

# res = a[: 3]
# res = a[2: 4]
# res = a[4: 9]

# cnt = len(a)
# res = a[cnt-1]

# res = a[-3]
# res = a[-5: -2: 2]
# for i in range(-5, -2, 2):
#     print(a[i])

res = a[-2: -5: -1]

print(f"res: {res}")
