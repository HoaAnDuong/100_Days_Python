import turtle
from PIL import Image
import numpy
from pynput import keyboard
import time

img = Image.open("Lively Bottle.png")
img = numpy.array(img)

class MyTurtle(turtle.Turtle):
    def paintFromImage(self, image, pos = (0,0), step = 16,size = 5,detail_mode = 0):
        turtle.tracer(False)
        turtle.colormode(255)
        self.penup()
        self.speed("fastest")
        num_rows = len(image)
        num_cols = len(image[0])

        for i in range(num_rows):
            if i % step == 0:
                exe_time = time.time()

                self.setpos(pos[0],pos[1]-i/(step/size))
                self.setheading(0)
                if detail_mode > 0: turtle.update()
                for j in range(num_cols):
                    if j % step == 0:
                        self.dot(size,img[i][j])
                        self.forward(size)
                        if detail_mode > 1: turtle.update()
                exe_time = time.time() - exe_time
                print("{}% (Paint rate: {}%/s)".format(((i+step)/num_rows)*100,((step/num_rows)*100)/exe_time))
        turtle.update()
        turtle.Screen().exitonclick()






screen = turtle.Screen()
my_turtle = MyTurtle()
turtle.colormode(255)
my_turtle.paintFromImage(img,pos = (-256,256),step = 8,size = 5,detail_mode=1)


