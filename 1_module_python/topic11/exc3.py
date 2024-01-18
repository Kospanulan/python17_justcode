
class GreaterThanTen(Exception):
    pass


def get_sum(a, b):
    if a > 10 or b > 10:
        raise GreaterThanTen('a или b больше чем 10!')
    return a + b


print('Старт программы!')

# res = get_sum(5, 11)
# print(res)

try:
    res = get_sum(5, 11)
    print(res)
except ValueError as ex:
    print(f'В программе была ошибка! {ex}')
# except Exception as ex:
#     print(f'Ошибка, но не знаю какая;(')


print('Конец программы!')





