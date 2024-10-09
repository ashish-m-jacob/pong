from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(n=0)

# Creating paddles
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

# Creating the ball
ball = Ball()

# Creating the scorecard
scorecard = Scorecard()

# Listening for key events
screen.listen()

# left paddle moving
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

# right paddle moving
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detecting ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detecting collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()



    # Detecting left paddle miss
    if ball.xcor() < -350:
        ball.ball_reset()
        scorecard.r_point()



    # Detecting right paddle miss
    if ball.xcor() > 350:
        ball.ball_reset()
        scorecard.l_point()





screen.exitonclick()