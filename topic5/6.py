#     *     - 4 = 5 - 1   i = 0
#    * *    - 3 = 5 - 2   i = 1
#   * * *   - 2 = 5 - 3   i = 2
#  * * * *  - 1 = 5 - 4   i = 3
# * * * * * - 0 = 5 - 5   i = 4

n = 5
# for i in range(n-1, -1, -1):
for i in range(n):
    for j in range(n - (i+1)):
        print("-", end="")

    for j in range(i+1):
        print("*", end=" ")
    print()





