# Пн Вт Ср Чт Пт Сб Вс
# 0  1   2  3  4  5  6

from datetime import datetime, timezone, timedelta

str_datetime = '2024/01/01 01:25:45'

datetime_obj = datetime.strptime(str_datetime, '%Y/%m/%d %H:%M:%S')


print(f"День недели: {datetime_obj.weekday()}")






