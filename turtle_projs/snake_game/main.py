from snake import Snake
import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

x_wall, y_wall = 300,300
UP = 90
DOWN=270
LEFT =180
RIGHT =0

class Game:
    def __init__(self):
        self.sc = Screen()
        self.sc.setup(height=600, width=600)
        self.sc.bgcolor("black")
        self.sc.title("Snake game")
        self.sc.tracer(0)

        self.s1 = Snake()
        self.start_listening()
    
    def move_up(self):
        if self.s1.snake[0].heading() != DOWN:
            self.s1.snake[0].setheading(90)

    def move_down(self):
        if self.s1.snake[0].heading() != UP:
            self.s1.snake[0].setheading(270)

    def move_right(self):
        if self.s1.snake[0].heading() != LEFT:
            self.s1.snake[0].setheading(0)

    def move_left(self):
        if self.s1.snake[0].heading() != RIGHT:
            self.s1.snake[0].setheading(180)

    def start_listening(self):
        self.sc.listen()
        self.sc.onkeypress(self.move_right, "Right")
        self.sc.onkeypress(self.move_up, "Up")
        self.sc.onkeypress(self.move_down, "Down")
        self.sc.onkeypress(self.move_left, "Left")

    def play(self):
        food = Food(self.s1.snake) 
        sb = Scoreboard()
        while True:
            self.sc.update()
            self.s1.move()
            time.sleep(0.1)

            if self.s1.snake[0].distance(food) < 15:
                #print("nom nom nom")
                food.appear(self.s1.snake)
                sb.update()
                self.s1.grow()
            if self.s1.isGameOver(x_wall,y_wall):
                sb.gameOver()
                
                break

        self.sc.mainloop()


if __name__ == '__main__':
    snakeGame= Game()
    snakeGame.play()
