from turtle import Turtle
from food import Food
import random

ALIGNMENT = "center"
FONT_STYLE = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(0, 270)
        self.update_Score()

    def update_Score(self) :   
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_STYLE)
        
    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT_STYLE)

    def increase_Score(self):
        self.score += 1
        self.goto(0, 270)
        self.clear()
        self.update_Score()