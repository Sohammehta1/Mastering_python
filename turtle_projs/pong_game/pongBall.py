from turtle import Turtle
import random


y_limit = 300
x_limit = 400

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        # self.fillcolor("white")
        self.speed(0)
        self.gameOver = False
        self.xchange = 3
        self.ychange = 3
        
        
        # self.setheading((random.choice([-1,1]))*random.randint(0,180))


    def move(self):
        
        self.goto(self.xcor()+self.xchange,self.ycor()+self.ychange)

    def bounce(self, paddle1, paddle2):
        
        x, y = self.pos()
        if self.distance(paddle1.pos()) < 30 or self.distance(paddle2.pos()) < 30:
            self.xchange *= -1   # Reverse x direction on paddle collision
        if y >= y_limit or y <= -y_limit:
            self.ychange *= -1  # Reverse y direction on top/bottom collision
        if x >= x_limit or x <= -x_limit:
            self.gameOver = True  # Game over on left/right collision
            return "l" if x >= x_limit else "r"
            
        

        
            
    def reset(self):
        self.goto(0,0)
        self.gameOver = False
        self.xchange = 3
        self.ychange = 3
        

        