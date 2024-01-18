

class Wardrobe:

    def __init__(self):
        self.door = 'Closed'

    def open_door(self):
        self.door = 'Open'
        print('Мы открыли дверь...')

    def get_candy(self):
        if self.door == 'Closed':
            print("Дверь закрыта!")
        else:
            print('Мы взяли конфеты...')

    def close_door(self):
        self.door = 'Closed'
        print('Мы закрыли дверь...')

    def __enter__(self):
        self.open_door()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_door()


with Wardrobe() as shkafchik:
    shkafchik.get_candy()


shkafchik.get_candy()
print("Конец программы!")

# shkafchik = Wardrobe()
#
# shkafchik.open_door()
#
# shkafchik.get_candy()
#
# shkafchik.close_door()

