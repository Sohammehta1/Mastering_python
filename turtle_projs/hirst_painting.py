import colorgram as cg
import turtle as tt
from turtle import colormode
from common_functions import *

colormode(255)

color_pallete = cg.extract('turtle_projs/Damien-Hirsts-Spot-Painting-1986.jpg',50)

colors =[]
for c in color_pallete:
    colors.append(c.rgb)
print(colors)

red = tt.Turtle()
red.pencolor(pickThreeColors(colors))
red.width(10)

red.circle(100)

red.screen.mainloop()