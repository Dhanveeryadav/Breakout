from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(1, 5)
        self.penup()
        self.goto(position)

    def right_side(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def left_side(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

