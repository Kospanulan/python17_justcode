# Дано радиус r, нужно найти площадь окружности по формуле
# S = π × r^2 .

import math


# S = π × r^2
def get_area(r):
    return math.pi * math.pow(r, 2)


# V = 4/3 × π × r^3
def get_volume(r):
    return 4/3 * math.pi * math.pow(r, 3)


print(f"1. area: {get_area(5)}")
print(f"2. volume: {get_volume(5)}")
print(f"3. radians: {math.radians(360)}")


