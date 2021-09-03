from turtle import Turtle


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.rem_lives = f"X{self.lives}"
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.goto(-380, -200)
        self.write(self.rem_lives, align="left", font=("ariel", 24, "normal"))

    def lives_left(self):
        self.lives -= 1
        self.rem_lives = f"X{self.lives}"
        self.update_lives()
