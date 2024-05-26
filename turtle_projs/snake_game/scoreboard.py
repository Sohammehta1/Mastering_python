from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"score : {0}",align="center",font=("Arial",20,"normal"))

    def update(self):
        self.clear()
        self.score  += 10
        self.write(f"score : {self.score}", align="center",font=("Arial",20,"normal"))

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",20,"normal"))