from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PINGPONG")
screen.tracer(0)

# Creating Paddle objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


# Screen Listen methods
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=l_paddle.up, key="w")

# Creating ball object
ball = Ball()

# Creating scoreboards objects
r_paddle_score = Scoreboard((50, 220))
l_paddle_score = Scoreboard((-50, 220))


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #  R_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        l_paddle_score.update_score()

    # L_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        r_paddle_score.update_score()

    # Detection with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detection with the paddle
    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()












































screen.exitonclick()
