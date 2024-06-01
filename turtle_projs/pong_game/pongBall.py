from turtle import Turtle
import random 


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.fillcolor("white")
        self.speed(0)
        self.gameOver = False
        
        self.setheading((random.choice([-1,1]))*random.randint(0,180))


    def move(self):
        self.forward(3)

    def bounce(self):
        self.left(random.randint(0,30))
        
    def isGameOver(self, t1: Turtle, t2:Turtle):
        x,y = self.pos()
        if 400-abs(x) <=2:
            self.gameOver = True
            return True
        if self.distance(t1.pos())<=25 or self.distance(t2.pos())<=25:
            self.left(45)
            # self.bounce()
        elif  300-abs(y)<=10:
            self.left(45)
            
    def reset(self):
        self.goto(0,0)
        self.setheading((random.choice([-1,1]))*random.randint(0,180))

        