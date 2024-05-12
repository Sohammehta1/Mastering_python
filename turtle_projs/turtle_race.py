import random 
from turtle import Turtle, colormode, Screen

colormode(255)

Tim = Turtle(shape="turtle")
John = Turtle(shape="turtle")
Uday = Turtle(shape="turtle")
Mahesh = Turtle(shape="turtle")
Jethalal = Turtle(shape="turtle")

participants=[Tim,John,Uday,Mahesh,Jethalal]
colors = ['violet','blue','indigo','green','red',]

sc = Screen()
sc.setup(600,400)
x = -280
y = -170
userbet = sc.textinput(title="bet",prompt="Which color are you betting on?")
for i in range(len(participants)):
    participants[i].color(colors[i])
    participants[i].penup()
    participants[i].goto(x,y)
    participants[i].speed(1)
    y = y + 70

race_over = False

while not race_over:
    for turtle in participants:
        turtle.forward(random.randint(1,10))
        x, y = turtle.position()
        if x >=300: # turtle wins
            race_over = True
            cr = turtle.color()[0]
            print(f"The winner is {cr}")
            if cr == userbet:
                print("Congrats, You won the bet!")
            else:
                print("You lost the bet!")

sc.mainloop()