
password = 'qwerty123'

user_input = input("Введите пароль: ")

password_matched = True
number_attempts = 3

while user_input != password:
    number_attempts = number_attempts - 1
    if number_attempts == 0:
        password_matched = False
        break

    print(f"Извините, но пароль не совпадает! Осталось попыток {number_attempts}")
    user_input = input("Введите пароль: ")


if password_matched is True:
    print("Пароль верный.")
else:
    print(f"У вас не осталось попыток!")
