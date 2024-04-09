from turtle import Screen
from turtle_crossing_game_turtle_behaviour import Player
import time


screen = Screen()
screen.title("Turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
tur_tle = Player((0, -280))
screen.listen()
screen.onkeypress(key="Up", fun=tur_tle.move_up)

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
