# here we have to make a spirograph with each circle of different color

import turtle as t
from turtle import Screen
import random


shin = t.Turtle()
t.colormode(255)
shin.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for i in range(int(360 / 5)):
    shin.color(random_color())
    shin.circle(100)
    shin.left(5)

screen = Screen()
screen.exitonclick()
