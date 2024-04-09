from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() < 280:
            new_ycor = self.ycor() + 20
            self.goto(0, new_ycor)
