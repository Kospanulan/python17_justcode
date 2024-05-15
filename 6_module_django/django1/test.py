# import sys
#
# print(f"Hello {sys.argv[-1]}!")
import time


def get_time(*args, **kwargs):
    def wrapper(my_func):
        print(kwargs)
        print(my_func)
        print("starting in decorator...")
        start_time = time.time()
        my_func()
        run_time = time.time() - start_time
        print(f"finished in decorator in {run_time}!")

    return wrapper


@get_time(commands='start')
def say_hello():
    print("Hello")


@get_time(commands='end')
def say_hi():
    print("Hi")


say_hello()

say_hi()


# print("starting...")
# start_time = time.time()
# say_hello()
# run_time = time.time() - start_time
# print(f"finished in {run_time}!")
#
# print("============")
#
# print("starting...")
# start_time = time.time()
# say_hi()
# run_time = time.time() - start_time
# print(f"finished in {run_time}!")
