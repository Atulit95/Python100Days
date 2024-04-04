from turtle import Screen
from padles import Paddles
from Pong_Game_Ball import Ball
import time

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

game_is_on = True

l_paddle = Paddles((-485, 0))
r_paddle = Paddles((475, 0))
ball = Ball()

screen.listen()
screen.onkeypress(l_paddle.goup, "w")
screen.onkeypress(l_paddle.godown, "s")
screen.onkeypress(r_paddle.goup, "Up")
screen.onkeypress(r_paddle.godown, "Down")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
