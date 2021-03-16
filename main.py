from turtle import Turtle, Screen
from padle import Paddle
from ball import Ball
from scoreboard import Score_board
import time


screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)


r_paddle = Paddle((355,0))
l_paddle = Paddle((-355,0))
ball = Ball()
scoreboard= Score_board()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collison wall
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collison with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()


