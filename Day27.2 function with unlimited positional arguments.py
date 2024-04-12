# Here the in the word "*args". The impoatant part is :
# '*' sign  denotes that  this function can take any number of arguments
# The word "args" is not important it can be of user choice but it is preferable
# this "args" is in form of tuple


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5))
