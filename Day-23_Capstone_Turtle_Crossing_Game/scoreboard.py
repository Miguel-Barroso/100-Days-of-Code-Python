from turtle import Turtle


FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.setpos(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)