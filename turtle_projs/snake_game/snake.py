from turtle import Turtle

MOVE_DISTANCE = 20
class Snake:

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed(0)
        
        new_segment.goto(self.snake[-1].position())
        self.snake.append(new_segment)
        #print(len(self.snake))
        #print("hey")
        
    def create_snake(self):
        for i in range(2):
            self.add_segment()
            #self.snake.append(self.snake[i])

    def __init__(self):
        self.snake = [Turtle(shape="square") ]
        self.snake[0].color("white")
        self.snake[0].penup()
        self.snake[0].speed(0)
        self.create_snake()
        

    def grow(self): # APPENDING SEGMENTS AFTER EATING FOOD
        self.add_segment()
        
    def move(self):    
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)
            
        #snake[0].left(90)

    

    def isGameOver(self,x_wall,y_wall):
        x,y = self.snake[0].pos()
        x,y = abs(x), abs(y)

        if x>=x_wall  or y >=y_wall :
            return True
        else:
            x,y = self.snake[0].pos()
            for segment in self.snake[2:]:
                if segment.distance(x,y)<10:
                    return True
        return False






                


# if __name__ == "__main__":
#     s1 = Snake()