# * * * * *
#  * * * *
#   * * *
#    * *
#     *

n = 5
# for i in range(n-1, -1, -1):
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("*", end=" ")

    print()


# n = 5
# for i in range(n-1, -1, -1):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end=" ")
#
#     print()
