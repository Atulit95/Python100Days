from turtle import Screen
from turtle_crossing_game_turtle_behaviour import turtle_with_behaviour

screen = Screen()
screen.title("Turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)

tur_tle = turtle_with_behaviour()

screen.update()
screen.exitonclick()
