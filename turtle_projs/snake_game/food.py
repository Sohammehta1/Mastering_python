from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self,snake:list) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.appear(snake)

    def appear(self,snake:list):
        while True:
            random_x = random.randint(-280,280)
            random_y = random.randint(-280,280)
            intercepting  = True
            for segment in snake:
                x,y = segment.pos()
                if random_x   != x and random_y != y:
                    intercepting = False
                    break
            if not intercepting:
                break
        self.setpos(random_x,random_y)
