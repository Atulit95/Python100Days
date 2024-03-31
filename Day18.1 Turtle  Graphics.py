# Here our goal is to draw shapes from triangle to decagon with same base and different color every time

from turtle import *


shin = Turtle()
shin.shape("turtle")
shin.color("violet")
shin.teleport(x=-50, y=200)
turtle_colors = ["green", "brown", "olive", "yellow", "gray", "red", "orange", "black"]
for i in range(3, 11):
    for j in range(0, i):
        shin.fd(100)
        shin.color(turtle_colors[i - 3])
        shin.right(360 / i)

screen = Screen()
screen.exitonclick()
