import random
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.score = 0
        self.write("Score: 0", font=("Monospace", 12, "bold"))

    def update_score(self):
        self.clear()
        self.write("Score: " + str(self.score), font=("Monospace", 12, "bold"))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=("Monospace", 12, "bold"))

        




