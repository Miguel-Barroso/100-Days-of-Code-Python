from turtle import Turtle

PADDLE_WIDTH = 20  # Value in pixels
PADDLE_HEIGHT = 100  # Value in pixels
MOVE_DISTANCE = 25  # The amount to move the paddle

class Paddle(Turtle):

    def __init__(self, starting_coordinates):
        super().__init__()  # To get all the features of the Turtle class initiated
        self.color("white")
        self.shape("square")  # Without calling the shape function, you'll get an arrow
        self.shapesize(stretch_wid=(20 / 4), stretch_len=(100 / 100))  # Sizes are factors of 20
        self.penup()
        self.goto(starting_coordinates)

    def up(self):
        if self.ycor() >= 240:
            pass
        else:
            self.goto(self.xcor(), self.ycor() + 25)

    def down(self):
        if self.ycor() <= -240:
            pass
        else:
            new_y_pos = self.ycor() - 25
            self.goto(self.xcor(), new_y_pos)
