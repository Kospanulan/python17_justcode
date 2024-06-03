import time


class Animal:

    sound = None

    def say_something(self):
        print(self.sound)




class Cat(Animal):

    sound = "Myau-myau"

    # def say_something(self):
    #     super().say_something()
    #     time.sleep(3)
    #     print("That's it")


cat = Cat()

cat.say_something()



print(Cat)
print(Cat())
print(cat)









