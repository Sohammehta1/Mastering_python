import random
import turtle as tt
from turtle import colormode
from common_functions import *



colormode(cmode=255)

center_turtle= tt.Turtle()
center_turtle.penup()

radius = 100
red = tt.Turtle()
sc = tt.Screen()
red.circle(radius)
red.penup()
x,y =red.position()
red.goto(x+10,y+10)
red.pendown()
red.circle(radius)
sc.exitonclick()