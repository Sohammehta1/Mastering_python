from turtle import Turtle,  Screen
import time
x_wall, y_wall = 300,300
UP = 90
DOWN=270
LEFT =180
RIGHT =0

def move(snake):    
    for i in range(1,len(snake)):
        new_pos = snake[i-1].pos()
        snake[i].setpos(new_pos)
    snake[0].forward(20)
        
    #snake[0].left(90)

  

def isGameOver(snake):
    x,y = snake[0].pos()
    x,y = abs(x), abs(y)
    if x>=x_wall  or y >=y_wall :
        return True
    return False





def playGame():
    sc = Screen()
    sc.setup(height=600, width=600)
    sc.bgcolor("black")
    sc.title("Snake game")
    sc.tracer(0)
    snake = [Turtle(shape="square") for i in range(3)]
    x,y=0,0
    for i in range(3):
        
        snake[i].color("white")
        snake[i].penup()
        snake[i].speed(0)
        snake[i].setpos(x,y)
        x -=25
        snake.append(snake[i])


    def move_up():
        if snake[0].heading() != DOWN:
            snake[0].setheading(90)

    def move_down():
        if snake[0].heading() != UP:
            snake[0].setheading(270)

    def move_right():
        if snake[0].heading() != LEFT:
            snake[0].setheading(0)

    def move_left():
        if snake[0].heading() != RIGHT:
            snake[0].setheading(180)

    # Now moving the snake
    sc.listen()
    sc.onkeypress(move_right, "Right")
    sc.onkeypress(move_up, "Up")
    sc.onkeypress(move_down, "Down")
    sc.onkeypress(move_left, "Left")
    

    while True:
        sc.update()
        move(snake)
        time.sleep(0.1)
        if isGameOver(snake):
            print("Game over!")
            break
            




    sc.mainloop()

if __name__ == "__main__":
    playGame()