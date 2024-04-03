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

    # Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_Score()
        score.update_Score()
        snake.extend()

    # Detect Collision with Walls

    if (
        snake.head.xcor() > 290
        or snake.head.ycor() > 267
        or snake.head.xcor() < -280
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        score.gameOver()

    # Detect collision with Tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.gameOver()

screen.exitonclick()
