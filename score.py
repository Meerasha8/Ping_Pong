from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l=0
        self.score_r=0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100,180)
        self.write(self.score_l, align="center", font=("arial", 80, "normal"))
        self.goto(100,180)
        self.write(self.score_r, align="center", font=("arial", 80, "normal"))
    def r_point(self):
        self.score_r+=1
        self.update()
    def l_point(self):
        self.score_l+=1
        self.update()
    def display_winner(self,display):
        self.goto(0,0)
        self.write(display,align="center",font=("arial",60,"normal"))


