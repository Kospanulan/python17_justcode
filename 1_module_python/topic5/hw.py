# XOXOXO
# OXOXOX
# XOXOXO
# OXOXOX


for i in range(4):
    for j in range(6):
        if (i + j) % 2 == 0:
            print('X', end='')
        else:
            print('O', end='')
    print()


