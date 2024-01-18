# file = open("test.txt", 'r')
#
# data = file.read()
# print(data)
#
# file.close()
# ===================================

with open("test.txt", 'r') as file:  # alias - псевдоним
    data = file.read()

# file.read()
print(data)


