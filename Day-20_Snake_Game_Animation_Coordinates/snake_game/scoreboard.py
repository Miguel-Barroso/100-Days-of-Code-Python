from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as file:
            self.highscore = int(file.read())
        self.shape("blank")
        self.color('white')
        self.penup()
        self.setpos(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Scoreboard: {self.score} Highscore: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        # self.clear()  Not going to use Game Over anymore
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setpos(0,0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
