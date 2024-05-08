import random
import turtle as tt
from turtle import colormode
from common_functions import *



colormode(cmode=255)

t = tt.Turtle()
t.speed(0)



def draw_spirograph(angular_displacement, turtle_obj, radius): # 't' is the turtle object
    head = turtle_obj.heading()
    loopCount = int(input("How many loops must be performed : "))
    iter_per_loop = 360//angular_displacement
    for _ in range(iter_per_loop*loopCount):
        turtle_obj.pencolor(pickThreeColors())
        turtle_obj.circle(radius)
        head += angular_displacement
        turtle_obj.setheading(head)


draw_spirograph(angular_displacement=5, turtle_obj=t,radius=100)
print("Loops compeleted!")
t.screen.mainloop()