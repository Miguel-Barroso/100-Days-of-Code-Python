from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")


# i = 0
# while i < 4:
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#     i += 1

# for _ in range(50):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.up()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.down()

def get_angle(sides):
    angle = (360 / sides)
    return angle


sides = 3
while sides < 21:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy_the_turtle.color(r, g, b)
    for _ in range(sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(get_angle(sides))
    sides += 1


screen.exitonclick()
