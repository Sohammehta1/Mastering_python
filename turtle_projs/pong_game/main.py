from turtle import Turtle,Screen
from scoreboard import Scoreboard

def DrawDashedLine(turtle:Turtle):
    turtle.color("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,300)
    turtle.pendown()
    turtle.pensize(10)

    
    turtle.setheading(270)
    blank = False
    while turtle.distance(0,-300) >10:
        if not blank:
            turtle.pendown()
        else:
            turtle.penup()
        blank = not blank   
        turtle.forward(20)
        
        

def playPong():
    sc = Screen()
    sc.setup(height=600,width=800)
    sc.bgcolor("black")
    t = Turtle()
    DrawDashedLine(t)
    score_left = Scoreboard((-30,260))
    score_right = Scoreboard((30,260))
    
    sc.mainloop()
    

if __name__ == "__main__":
    playPong()