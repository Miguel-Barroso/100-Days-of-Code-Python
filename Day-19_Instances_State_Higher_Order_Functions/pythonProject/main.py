from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

tim.setheading(270)

screen.listen()
screen.onkey(key="w", fun=move_forward) # Func() would trigger the function, here it's just passed as an argument.
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="space", fun=tim.reset)





screen.exitonclick()
