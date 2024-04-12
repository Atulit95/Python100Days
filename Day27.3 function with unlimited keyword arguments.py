# Here the in the word "**kwargs". The impoatant part is :
# '**' sign  denotes that  this function can take any number of keyword arguments
# The word "kwargs" is not important it can be of user choice but it is preferable
# this "args" is in form of dictionary


def calculate(n, **kwargs):
    # print(kwargs)   to check the type of kwargs
    n += kwargs["add"]
    n *= kwargs["mul"]


#     print(n)


# print(calculate(5, add=2, mul=5))


class Car:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="nisan", model="GTr")
# print(my_car.make)


# if we dont pass second aregumnent in above code
# it going to give us key error to avoid this error we use
# get() method it is same as square brackets but instead of error it will give us value "None"

# my_car2 = Car(make="Hyundai")


class Car2:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car3 = Car2(make="Hyundai")

print(my_car3.model)
