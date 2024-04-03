from turtle import Turtle
from food import Food
import random


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(0, 280)
        self.write(
            f"Score: {self.score}", True, align="center", font=("Arial", 15, "normal")
        )
