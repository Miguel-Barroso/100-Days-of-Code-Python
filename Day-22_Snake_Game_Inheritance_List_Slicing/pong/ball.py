from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.08  # Sets the time delay of the game loop

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1  # Bounces the ball vertically

    def bounce_x(self):
        self.move_x *= -1  # Bounces the ball horizontally
        self.move_speed *= 0.9  # Increases the move speed for every paddle hit

    def reset_position(self):
        self.goto(0, 0)
        print("New Ball")
        self.bounce_x()
        self.move_speed = 0.08
