def add(*args):  # Args could be anything, the * is what is important
    sum = 0
    for n in args:  # Arguments are stored as a tuple which can be accessed through a loop like this or by index
        sum += n
    return sum

print((1, 2, 3))

# def calculate(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#         print(kwargs["add"])
#
# calculate(add=3, multiply=5)


def calculate(n, **kwargs):  # Positional arguments can be combined with key word arguments (!)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):  # Optional key word arguments added to the init function of a class (kw can be anything)
        self.make = kw["make"]  # Using [] and then not specifying the key when calling the function results in a KeyErr
        self.model = kw.get("model")  # By using get() instead, it will return None and the program will continue


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)  # 4 is passed by position. 7,3,0 are collected into a tuple. x and y are
                                             # in a keyword dictionary