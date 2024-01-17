
class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        # return self.a * self.a
        return pow(self.a, 2)

    def get_perim(self):
        return self.a * 4

    def __lt__(self, other):  # less than '<'
        print(f'called __lt__()...')
        print(f'{self = }')
        print(f'{other = }')
        return self.a < other.a

    def __gt__(self, other):  # greater than '>'
        print(f'called __gt__()...')
        print(f'{self = }')
        print(f'{other = }')
        return self.a > other.a

    def __repr__(self):
        return f'Квадрат со строной {self.a} см.'


sq1 = Square(5)
sq2 = Square(7)

if sq1 > sq2:  # sq2 < sq1
    print('sq1 больше')
else:
    print('sq2 больше')

# if sq1 < sq2:  # sq1 < sq2
#     print('sq1 меньше')
# else:
#     print('sq2 меньше')







