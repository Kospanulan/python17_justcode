import random

first_user_name = input("first user: ")
second_user_name = input("second user: ")


first_user = random.randint(1, 6)
second_user = random.randint(1, 6)

print(f"{first_user_name}: {first_user}\n{second_user_name}: {second_user}")

if first_user > second_user:
    print(f"the winner is {first_user_name} !")
elif first_user < second_user:
    print(f"the winner is {second_user_name} !")
else:
    print("Draw!")
