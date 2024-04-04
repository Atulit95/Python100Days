from turtle import Turtle

PADDLES_POSITION = ((450, 0), (-450, 0))


class Paddles(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def goup(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def godown(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)
