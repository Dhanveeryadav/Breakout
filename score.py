from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.score = f"Score:{self.user_score}"
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(380, -200)
        self.write(self.score, align="right", font=("ariel", 24, "normal"))

    def inc_score(self):
        self.clear()
        self.user_score += 1
        self.score = f"Score:{self.user_score}"
        self.update_score()

    def result(self):
        self.write(f"Your {self.score}", align="center",  font=("ariel", 24, "normal"))