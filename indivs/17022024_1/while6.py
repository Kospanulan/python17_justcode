# %, //

n = "12345"

n_list = list(n)
# print(n_list)

reversed_list = []

i = len(n_list) - 1
while i >= 0:
    print(n_list[i])
    reversed_list.append(n_list[i])

    i -= 1


reversed_list = "".join(reversed_list)
print(reversed_list)

