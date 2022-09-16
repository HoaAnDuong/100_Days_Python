
import turtle
import random
import time
random.seed(time.time())

class Food(turtle.Turtle):
    def __init__(self):
        turtle.tracer(False)
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5)

    def tp(self,tp_range):
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.setpos(random.randint(-(tp_range[0]-20)/20,(tp_range[0]-20)/20)*10,random.randint(-(tp_range[1]-20)/20,(tp_range[1]-20)/20)*10)
        turtle.update()

