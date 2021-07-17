from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("deeppink3")
        self.penup()
        self.bounce_is_on = True
        self.change_in_x = 10
        self.change_in_y = 10
        self.move_speed = 0.1        #referring to seconds in time.sleep()





    def move_ball(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor + self.change_in_x, y_cor + self.change_in_y)

    def bounce_y(self):
        self.change_in_y *= -1


    def bounce_x(self):
        self.change_in_x *= -1
        self.move_speed *= 0.9



    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()















