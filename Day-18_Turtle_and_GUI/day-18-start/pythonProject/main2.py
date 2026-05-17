import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

tim.pensize(10)
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(200):

    tim.color(random_color())
    angle = 90 * random.randint(0, 3)
    tim.setheading(angle)
    tim.forward(25)

screen = t.Screen()
screen.exitonclick()
