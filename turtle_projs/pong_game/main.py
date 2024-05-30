from turtle import Turtle,Screen
from scoreboard import Scoreboard
from paddle import Paddle
from threading import Thread
from pongBall import Ball

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
        while t.distance(0,-300) >10:
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
        
        self.DrawDashedLine()
        score_left = Scoreboard((-30,260))
        score_right = Scoreboard((30,260))
        left_paddle = Paddle(is_left=True)
        right_paddle = Paddle()
        b = Ball()
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
        
        def play():
            if not self.playing:
                self.playing = True
                
                while True:
                    sc.update()
                    left_paddle.move()
                    right_paddle.move()
                    b.move()
                    if b.isGameOver(left_paddle,right_paddle):
                        if b.gameOver: # This round is over, now we will update the scoreboard and reset position
                            x,y = b.pos()
                            if x < 0:
                                score_right.updateScore()
                            else:
                                score_left.updateScore()
                            # Now we need to reset the positions
                            left_paddle.reset()
                            right_paddle.reset()
                            b.reset()
                            self.playing = False
                            return
                    
                    if left_paddle.gameOver():
                        self.playing = False
                        return 
            else:
                return

        sc.onkeypress(fun=left_paddle.up,key='w')
        sc.onkeypress(fun=left_paddle.down,key='s')
        sc.onkeypress(fun=right_paddle.up,key="Up")
        sc.onkeypress(fun=right_paddle.down,key="Down" )
        sc.onkeypress(fun=play,key="space")
       
        
        sc.mainloop()
    

if __name__ == "__main__":
  pong = PlayGame()
  pong.playPong()