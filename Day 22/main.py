from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

ball = Ball((0,0))
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(right_paddle.go_up,"Up")
screen.onkeypress(right_paddle.go_down,"Down")

screen.onkeypress(left_paddle.go_up,"w")
screen.onkeypress(left_paddle.go_down,"s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#collision with right and left paddle:
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

# detect when right paddle misses

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect when left paddle misses
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()







# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)
#
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(),new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(),new_y)
#
#
# screen.listen()
# screen.onkey(go_up,"Up")
# screen.onkey(go_down,"Down")
