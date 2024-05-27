from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score =0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.setpos(position)
        self.write(f"{self.score}",align="center",font=("Arial", 30, "normal"))
        print("hey")


    def updateScore(self):
        self.score +=1
        self.clear()
        self.write(f"{self.score}",align="center",font=("Arial", 30, "normal"))
    
    def gameOver(self,winner):
        self.goto(0,0)
        self.write(f"The winner is {winner}",align="center",font=("Arial", 30, "normal"))

