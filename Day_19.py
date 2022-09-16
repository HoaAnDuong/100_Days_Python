import turtle
import time
import random

random.seed(time.time())


class MyTurtle(turtle.Turtle):
    is_winning = False

def AbnormalTurtleRace():
    my_turtle = {}
    y_pos = 150
    for i in ["red","orange","yellow","green","blue","indigo","purple"]:
        my_turtle[i] = MyTurtle()
        my_turtle[i].speed(0)
        my_turtle[i].penup()
        my_turtle[i].color(i)
        my_turtle[i].setpos(-300,y_pos)
        my_turtle[i].setheading(0)
        y_pos-=50
    predict_turtle = ''
    while True:
        if not predict_turtle in my_turtle:
            predict_turtle = input("Enter your bet turtle: (red,orange,yellow,green,blue,indigo,purple):")
        else:
            break
    while True:
        chosen_turtle = random.choices(["red","orange","yellow","green","blue","indigo","purple"])[0]
        chosen_turtle = my_turtle[chosen_turtle]
        chosen_turtle.forward(random.randint(0,20))
        if chosen_turtle.xcor() >= 300:
            chosen_turtle.is_winning = True
            break
    my_turtle[predict_turtle].color("black")
    if my_turtle[predict_turtle].is_winning:
        print("Your Turtle({}) wins".format(predict_turtle))
    else:
        print("Your Turtle({}) loses".format(predict_turtle))

screen = turtle.Screen()
screen.setup(width = 1000, height = 600)
for i in range(3):
    AbnormalTurtleRace()
screen.exitonclick()