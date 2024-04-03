from turtle import Screen
import time
from snake import Snake
from food import Food
from SnakeGameScoreCard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game  ----===e  o")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(key="Up", fun=snake.turn_up)
screen.onkeypress(key="Down", fun=snake.turn_down)
screen.onkeypress(key="Left", fun=snake.turn_left)
screen.onkeypress(key="Right", fun=snake.turn_right)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score. += 1

screen.exitonclick()
