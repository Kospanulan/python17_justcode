import time

start_time = time.time()

print("Начинаем паузу...")
time.sleep(2)
print("Все!")

end_time = time.time()
print(f"Программа выполнялась {int(end_time - start_time)} секунд.")


