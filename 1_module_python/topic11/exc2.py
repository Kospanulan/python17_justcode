
print('Старт программы!')

try:
    raise TypeError()
    # res = int('qw')
    res = int('456')
    # res = res / 0
    print(res)
except ValueError as ex:
    print(f'В программе была ошибка c преобразованием типов данных! {ex}')
except ZeroDivisionError as ex:
    print(f'В программе была ошибка c делением на ноль! {ex}')
except Exception as ex:
    print(f'Ошибка, но не знаю какая;(')
# else:
#     print('else... ошибки нет')
# finally:
#     print('finally...')

print('Конец программы!')

