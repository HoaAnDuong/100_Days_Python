from turtle import Turtle, Screen
import pynput
from pynput import keyboard
import time

class ControllableTurtle(Turtle):
    def active(self):
        self.speed(20)
        with keyboard.Events() as events:
            for e in events:
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
my_turtle = ControllableTurtle()
my_screen = Screen()
my_turtle.active()


