import turtle as t
from random import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("CadetBlue")
t.speed(100)

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    tim.right(angle)
    tim.forward(steps)
    

my_screen = t.Screen()
my_screen.exitonclick()

