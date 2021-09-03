from turtle import Turtle
from random import choice


class Brick(Turtle):
    colors = ["green", "orange", "yellow", "pink", "purple", "gold", "grey", "brown", "white"]

    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.turtlesize(1, 5)
        self.color(choice(self.colors))
        self.penup()
        self.goto(xpos, ypos)

