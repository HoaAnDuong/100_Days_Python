import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
    def update(self,score,pos):
        self.setpos(pos)
        self.clear()
        self.write("Score: {}".format(score), align="center", font=("Arial",24,"normal"))