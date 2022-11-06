from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.board()
    
    def board(self):
        self.clear()
        self.setpos(-280, 260)
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def update_level(self):
        self.level += 1
        self.board()
    
    def game_over(self):
        self.home()
        self.write("GAME OVER", align='center', font=FONT)