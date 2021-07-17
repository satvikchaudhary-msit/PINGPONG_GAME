from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1, 1)
        self.color("white")
        self.penup()
        self.goto(position)


    def up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor, y_cor + 20)


    def down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor, y_cor - 20)

