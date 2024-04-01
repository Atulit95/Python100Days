# Create a turtle race game in which you can bet on any turtle

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=500, width=600)
userbet = screen.textinput("Bet Counter", "Which turtle do you want to bet on?")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]

y_gap = 50
is_race_on = False
turtle_list = []

for turtles in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtles])
    new_turtle.goto(x=-280, y=200 - y_gap)
    y_gap += 50
    turtle_list.append(new_turtle)


if userbet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 278:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == userbet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")

        random_distace = random.randint(0, 10)
        turtle.fd(random_distace)


screen.exitonclick()
