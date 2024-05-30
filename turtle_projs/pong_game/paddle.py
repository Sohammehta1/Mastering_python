from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True,is_left=False) -> None:
        super().__init__(shape, undobuffersize, visible)
        
       
        self.color("white")
        self.speed(0)
        self.penup()
        self.isLeft = is_left
        if is_left:
            self.goto(-380,0)
        else:
            self.goto(380,0)
        self.sc = self.screen
        # rect_coords = ((6,-20),(6,20),(-6,20),(-6,-20))
        # Register the rectangle shape
        # self.sc.register_shape('rectangle', rect_coords)
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=3)
        self.setheading(90)
        self.distance = 50
        
        

    def move(self):
        x,y = self.pos()
        if y >=300:
            self.forward(-self.distance)
        if y<=-300:
            self.forward(self.distance)
    
    def up(self): 
        self.forward(self.distance)
    
    def down(self):
        self.forward(-self.distance)
        

    def gameOver(self):
        x,y = self.pos()
        return y>=300 or y <=-300

    def reset(self):
        if self.isLeft:
            self.goto(-380,0)
        else:
            self.goto(380,0)

    
    