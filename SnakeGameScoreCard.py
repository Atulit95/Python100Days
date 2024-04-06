from turtle import Turtle

ALIGNMENT = "center"
FONT_STYLE = ("Courier", 22, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(
            "snakeGame_data.txt", mode="r"
        ) as highest_score:  # (updated on day24)
            self.highscore = int(highest_score.read())
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(0, 267)
        self.update_Score()

    def update_Score(self):
        self.clear()
        self.write(
            f"Score: {self.score} | Highest Score: {self.highscore}",
            align=ALIGNMENT,
            font=FONT_STYLE,
        )

    def reset(self):  # added on day24
        if self.score > self.highscore:
            self.highscore = self.score
            with open("snakeGame_data.txt", mode="w") as highest_score:
                highest_score.write(f"{self.highscore}")
        self.score = 0

    # def gameOver(self):            # Commented on day24
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT_STYLE)

    def increase_Score(self):
        self.score += 1
        self.goto(0, 267)
        self.update_Score()
