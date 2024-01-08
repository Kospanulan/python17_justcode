
password = 'qwerty123'

number_attempts = 3
password_matched = False

for i in range(number_attempts):  # [0, 1, 2]
    user_input = input(f"Введите пароль. Осталось попыток {number_attempts-i}: ")

    if password == user_input:
        password_matched = True
        break

if password_matched is True:
    print("Пароль верный.")
else:
    print(f"У вас не осталось попыток!")
