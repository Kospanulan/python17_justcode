
import random

# random_number = random.randint(1, 1000)

# numbers = [1, 5, 7]
# numbers = ["hello", "world", "justcode"]
# random_number = random.choice(numbers)
# print(f"{random_number = }")

# numbers = [1, 5, 7]
# random_numbers = random.choices(numbers, k=4)
# print(f"{random_numbers = }")

numbers = ["hello", "world", "justcode", 1, 5, 7]
print(f"numbers: {numbers = }")
random.shuffle(numbers)
print(f"shuffled_numbers: {numbers}")

