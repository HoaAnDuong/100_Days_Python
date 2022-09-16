import turtle
import random
import time
from food import Food
from scoreboard import Scoreboard

class Snake:

    def __init__(self,length = 3,pos = (0,0)):
        turtle.colormode(255)
        turtle.tracer(False)
        turtle.bgcolor("black")

        self.score = 0

        self.barries_turtle = turtle.Turtle()

        self.segment = []
        self.segment.append(turtle.Turtle())
        self.segment[0].penup()
        self.segment[0].shape("square")
        self.segment[0].shapesize(0.5)
        self.segment[0].color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.segment[0].setpos(pos)

        for i in range(1,length):
            self.addSegment((self.segment[i-1].xcor()-10,self.segment[i-1].ycor()))

        turtle.update()
    def addSegment(self,pos):
        self.segment.append(turtle.Turtle())
        self.segment[-1].penup()
        self.segment[-1].shape("square")
        self.segment[-1].shapesize(0.5)
        self.segment[-1].color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.segment[-1].setpos(pos)
    def setup(self,playground,color = "white"):

        self.barries_turtle.penup()
        self.barries_turtle.shape("square")
        self.barries_turtle.shapesize(0.5)
        self.barries_turtle.pensize(10)
        self.barries_turtle.color(color)
        self.barries_turtle.setpos(-playground[0] / 2, -playground[1] / 2)
        self.barries_turtle.pendown()

        for i,j in enumerate([0,90,180,270]):
            self.barries_turtle.setheading(j)
            self.barries_turtle.forward(playground[(i)%2])


    def play(self, speed=10, playground=(500, 500), food = Food(),scoreboard = Scoreboard()):


        self.setup(playground)

        food.tp(playground)

        scoreboard.update(self.score,(0,playground[1]/2 - 50))

        turtle.update()

        # turtle.Screen().setup(width=playground[0], height=playground[1])
        turtle.Screen().onkey(self.right, "Right")
        turtle.Screen().onkey(self.up, "Up")
        turtle.Screen().onkey(self.left, "Left")
        turtle.Screen().onkey(self.down, "Down")
        turtle.Screen().listen()

        while True:
            prev_pos = self.segment[0].pos()
            self.segment[0].forward(10)
            for i in range(1, len(self.segment)):
                prev_pos_2 = self.segment[i].pos()
                self.segment[i].setpos(prev_pos)
                prev_pos = prev_pos_2


            if abs(self.segment[0].xcor()) >= playground[0] / 2 or abs(self.segment[0].ycor()) >= playground[1] / 2 :
                return self.died()
            for i in range(1, len(self.segment)):
                if int(self.segment[0].xcor()) == int(self.segment[i].xcor()) and int(self.segment[0].ycor()) == int(
                        self.segment[i].ycor()):
                    scoreboard.clear()
                    return self.died()

            if self.segment[0].xcor() >= food.xcor() - 5 and self.segment[0].xcor() <= food.xcor() + 5 and \
            self.segment[0].ycor() >= food.ycor() - 5 and self.segment[0].ycor() <= food.ycor() + 5:
                self.score += 1
                scoreboard.update(self.score, (0, playground[1]/2 - 50))
                food.tp(playground)
                self.addSegment(prev_pos)



            turtle.update()
            time.sleep(0.5 / speed)
    def right(self):
        self.segment[0].setheading(0)
        turtle.update()
    def left(self):
        self.segment[0].setheading(180)
        turtle.update()
    def up(self):
        self.segment[0].setheading(90)
        turtle.update()
    def down(self):
        self.segment[0].setheading(270)
        turtle.update()
    def died(self,color = "white"):
        for j in self.segment:
            j.color(color)
            turtle.update()
            time.sleep(0.05)

            j.hideturtle()
            turtle.update()
            time.sleep(0.05)
        self.barries_turtle.clear()
        turtle.update()
        print("Score:",self.score)
        return self.score

# screen = turtle.Screen()
# snake_1 = Snake(length = 20)
# snake_1.play(speed = 5)


