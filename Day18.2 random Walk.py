# Here the turtle will move same distance in any random direction(North, South, East, West)
# with different color every time
import turtle as t
from turtle import Screen
import random


shin = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


shin.pensize(10)
shin.speed("fastest")

direction = [0, 90, 180, 270]
for i in range(0, 1000):
    shin.fd(40)
    shin.color(random_color())
    shin.right(random.choice(direction))


screen = Screen()
screen.exitonclick()
