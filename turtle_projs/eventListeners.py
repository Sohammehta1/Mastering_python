import turtle as t
import random
from turtle import colormode
from common_functions import pickThreeColors

colormode(255)
x_limit = 400
y_limit = 400

wall_ahead = False
wall_behind =False
ceil_reached = False
floor_reached = False

def check_position(x,y):
    if x==x_limit or x == -x_limit:
        wall_ahead == True
    if y ==y_limit or y ==-y_limit:
        ceil_reached = True
    if x >x_limit and y >y_limit:
        sam.setpos(x_limit,y_limit)
    elif x > x_limit:
        sam.setpos(x_limit,y)
    elif y >y_limit:
        sam.setpos(x,y_limit)
    

def ahead():
    # x1,y1 = sam.position()
    # check_position(x1,y1)
    sam.width(random.randint(1,10))
    sam.pencolor(pickThreeColors())
    sam.fd(50)
    
    
def backwards():
    # x1,y1 = sam.position()
    # check_position(x1,y1)
    sam.width(random.randint(1,10))
    sam.pencolor(pickThreeColors())
    sam.back(50)

def turn_anticlockwise():
    sam.left(10)
def turn_clockwise():
    sam.right(10)   
        
def go_home():
    sam.penup()
    sam.home()
    sam.pendown()


sam = t.Turtle()
sc = sam.screen

x,y=sc.screensize()
sc.onkey(fun=ahead,key="w")
sc.onkey(key="s", fun = backwards)
sc.onkeypress(key='a', fun = turn_anticlockwise)
sc.onkeypress(key='d',fun=turn_clockwise)
sc.onkey(key='c', fun = sam.clear)
sc.onkey(key='u', fun = sam.penup)
sc.onkey(key='v',fun= sam.pendown)
sc.onkey(key='h', fun = go_home)

sc.listen()
sc.mainloop()