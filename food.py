import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # food defulat options
        self.shape("circle")
        self.color("blue")
        self.speed(0)
        self.new()

    def new(self):
        self.penup()
        x_pos = random.randrange(-280, 280)
        y_pos = random.randrange(-280, 280)
        self.goto(x_pos, y_pos)


