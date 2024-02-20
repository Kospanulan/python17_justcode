"""

n = 4, i = x        p = (n-1) - i

   *          i = 0, p = 3
  * *         i = 1, p = 2
 * * *        i = 2, p = 1
* * * *       i = 3, p = 0

n = 5
    *          i = 0, p = 4
   * *         i = 1, p = 3
  * * *        i = 2, p = 2
 * * * *       i = 3, p = 1
* * * * *      i = 3, p = 0

"""

n = 4
for i in range(n):

    p = (n - 1) - i
    print(' ' * p, end='')
    for j in range(n):
        print('*', end=' ')

        if j == i:
            break
    print()



