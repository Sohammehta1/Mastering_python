from turtle import Turtle,Screen
from scoreboard import Scoreboard
from paddle import Paddle
from threading import Thread
from pongBall import *
import time

class PlayGame():
    def __init__(self) -> None:
        self.playing = False
        pass

    def DrawDashedLine(self):
        t = Turtle()
        t.color("white")
        t.speed(0)
        t.hideturtle()
        t.penup()
        t.goto(0,300)
        t.pendown()
        t.pensize(7)

        
        t.setheading(270)
        blank = False
        while t.distance(0,-300) >=1:
            if not blank:
                t.pendown()
            else:
                t.penup()
            blank = not blank   
            t.forward(20)
        
        
    

    def playPong(self):
        sc = Screen()
        sc.setup(height=600,width=800)
        sc.bgcolor("black")
        sc.tracer(0)
        self.DrawDashedLine()
        score_left = Scoreboard((-30,260))
        score_right = Scoreboard((30,260))
        left_paddle = Paddle(is_left=True)
        right_paddle = Paddle()
        b = Ball()
        sc.tracer(1)
        sc.listen()
        # def thread_left():
        #     sc.onkeypress(fun=left_paddle.up,key='w')
        #     sc.onkeypress(fun=left_paddle.down,key='s')  

        # def thread_right():
        #     sc.onkeypress(fun=right_paddle.up,key="Up")
        #     sc.onkeypress(fun=right_paddle.down,key="Down" )   

        # th1 = Thread(target=thread_left())
        # th2 = Thread(target=thread_right())
        # th1.start()
        # th2.start()
        def reset():
            b.reset()
            left_paddle.reset()
            right_paddle.reset()
            self.playing  =False
        
        def play():
            if not self.playing:
                self.playing = True
                
                while True:
                    if self.playing == False:
                        return
                    sc.update()
                    # left_paddle.move()
                    # right_paddle.move()
                    b.move()
                    w= b.bounce(left_paddle, right_paddle)
                    if b.gameOver ==True:    
                        left_paddle.reset()
                        right_paddle.reset()
                        b.reset() 
                        if w =="r":
                            score_right.updateScore()
                        else:
                            score_left.updateScore()
                        self.playing = False    
                    
                    
            else:
                return

        sc.onkeypress(fun=left_paddle.up,key='w')
        sc.onkeypress(fun=left_paddle.down,key='s')
        sc.onkeypress(fun=right_paddle.up,key="Up")
        sc.onkeypress(fun=right_paddle.down,key="Down" )
        sc.onkeypress(fun=play,key="space")
        sc.onkeypress(fun=reset, key= "r")
       
        
        sc.mainloop()
    

if __name__ == "__main__":
  pong = PlayGame()
  pong.playPong()