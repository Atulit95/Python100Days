from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self, x_cor, y_cor) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(x_cor, y_cor)
        self.write(self.l_score, align=ALIGN, font=FONT)

    def l_scored(self):
        self.l_score += 1
        self.write(self.l_score, align=ALIGN, font=FONT)

    def r_scored(self):
        self.r_score += 1
        self.write(self.r_score, align=ALIGN, font=FONT)
