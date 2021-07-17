from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(position)
        self.write(arg=f"{self.score}", align="center", font=("Arial", 50, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", align="center", font=("Arial", 50, "normal"))
