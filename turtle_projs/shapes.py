import random
import turtle as tt 
from turtle import colormode
from common_functions import pickThreeColors
a = 4


def drawShape(sides, t): # 't' is the turtle object
    if 3<=sides<=10:
        angle = 360/sides
        for i in range(sides):
            t.forward(100)
            t.right(angle)


kohli = tt.Turtle()
my_screen = tt.Screen()
kohli.shape("turtle")
sides = 3 
colormode(cmode=255) # sets the number of bits allowed to represent each color


for i in range(3,11):
    
    kohli.pencolor(pickThreeColors()) # randomly picks 3 colors and assigns it to the pen
    drawShape(sides,kohli)
    sides += 1

my_screen.exitonclick()