import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG THE GAME")
screen.tracer(0)  # Turns off automatic updates of the screen which means we must explicitly call screen.update() to
# trace new information on the screen

# Create scoreboard
scoreboard = Scoreboard()

# Create the right paddle
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-375, 0))

# Create a ball
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)  # Pauses the execution of the loop, i.e., the screen update frequency
    ball.move()
    # Detect collision with wall
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.xcor() >= 350 and ball.distance(r_paddle) <= 50 or ball.xcor() <= -350 and ball.distance(l_paddle) <= 50:
        ball.bounce_x()
    # Detect ball out of bounds
    # Detect if right paddle missed
    if ball.xcor() >= 400 and ball.distance(r_paddle) >= 50:
        ball.reset_position()
        scoreboard.l_point()
    # Detect if left paddle missed
    if ball.xcor() <= -400 and ball.distance(l_paddle) >= 50:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
