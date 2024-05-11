import colorgram as cg
import turtle as tt
from turtle import colormode
from common_functions import *

colormode(255)

color_pallete = cg.extract('turtle_projs/Damien-Hirsts-Spot-Painting-1986.jpg',50)

colors =[]
for c in color_pallete:
    colors.append(c.rgb)
#print(colors)


red = tt.Turtle()

red.penup()
red.setpos(-200,-100)
red.pendown()

row_count = 10
column_count = 10
right = True
for _ in range(row_count):
    for __ in range(column_count-1):
        red.pencolor(pickThreeColors(colors))
        red.pendown()
        red.dot(20)
        red.penup()
        red.forward(50)
    red.pen(pickThreeColors(colors))
    red.dot(20)

    if right:
        red.left(90)
        red.forward(50)
        red.left(90)
        right = False
    else:
        red.right(90)
        red.forward(50)
        red.right(90)
        right= True
    



red.screen.mainloop()