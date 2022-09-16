import threading

import turtle
from pynput import keyboard
import random
import time
from threading import *

random.seed(time.time())

class MyTurtle(turtle.Turtle):

    def active(self):
        turtle.colormode(255)
        self.speed("fastest")
        self.pensize(10)
        with keyboard.Events() as events:
            while True:
                e = events.get(0.1)
                try:
                    self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    if e.key == keyboard.Key.esc and isinstance(e,keyboard.Events.Press):
                        return True
                    elif e.key == keyboard.Key.up and isinstance(e,keyboard.Events.Press):
                        self.setheading(90)
                        self.forward(10)
                    elif e.key == keyboard.Key.down and isinstance(e,keyboard.Events.Press):
                        self.setheading(270)
                        self.forward(10)
                    elif e.key == keyboard.Key.left and isinstance(e,keyboard.Events.Press):
                        self.setheading(180)
                        self.forward(10)
                    elif e.key == keyboard.Key.right and isinstance(e,keyboard.Events.Press):
                        self.setheading(0)
                        self.forward(10)
                except:
                    pass
    def wandering(self):
        turtle.colormode(255)
        self.speed("fastest")
        self.pensize(10)
        with keyboard.Events() as events:
            while True:
                e = events.get(0.00001)
                self.setheading(random.choice([0,90,180,270]))
                self.forward(10)
                try:
                    self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    if e.key == keyboard.Key.esc and isinstance(e, keyboard.Events.Press):
                        return True
                except:
                    pass
    def activeDot(self):
        turtle.colormode(255)
        self.speed("fastest")
        self.pensize(10)
        self.penup()
        with keyboard.Events() as events:
            while True:
                e = events.get(1)
                try:
                    self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    if e.key == keyboard.Key.esc and isinstance(e, keyboard.Events.Press):
                        self.pendown()
                        return True
                    elif e.key == keyboard.Key.up and isinstance(e, keyboard.Events.Release):
                        self.setheading(90)
                        self.dot(10)
                        self.forward(10)
                    elif e.key == keyboard.Key.down and isinstance(e, keyboard.Events.Release):
                        self.setheading(270)
                        self.dot(10)
                        self.forward(10)
                    elif e.key == keyboard.Key.left and isinstance(e, keyboard.Events.Release):
                        self.setheading(180)
                        self.dot(10)
                        self.forward(10)
                    elif e.key == keyboard.Key.right and isinstance(e, keyboard.Events.Release):
                        self.setheading(0)
                        self.dot(10)
                        self.forward(10)
                except:
                    pass
    def wanderingDot(self):
        turtle.colormode(255)
        self.speed("fastest")
        self.pensize(10)
        self.penup()
        with keyboard.Events() as events:
            while True:
                e = events.get(0)
                self.setheading(random.choice([0,90,180,270]))
                self.dot(10)
                self.forward(10)
                try:
                    self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    if e.key == keyboard.Key.esc and isinstance(e, keyboard.Events.Press):
                        self.pendown()
                        return True
                except:
                    pass
                time.sleep(0.01)






