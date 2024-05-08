import random
import turtle as tt
from turtle import colormode
from common_functions import pickThreeColors




def random_direction():
    angle= random.Random().choice([0,90,180,360])    
    return angle

myscreen = tt.Screen()
jolly  = tt.Turtle()
jolly.pensize(width=10)
jolly.speed(0)

for i in range(200):
    jolly.pencolor(pickThreeColors())
    jolly.forward(20)
    jolly.right(random_direction())

myscreen.exitonclick()
