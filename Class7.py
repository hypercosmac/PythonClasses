import turtle
import time

t = turtle.Turtle()
t2 = turtle.Turtle()

turtle.bgcolor("skyblue")

def go(x,y,n=t):
    n.penup()
    n.goto(x,y)
    n.pendown()

def winner():
    if t.pos()>= (300,250):
        go(-100,0)
        t.write("Player one wins!", font=("Arial",30,"bold"))
        time.sleep(2)
        turtle.bye()
    elif t2.pos()>= (300,-250):
        go(-100,0,t2)
        t2.write("Player two wins!",font=("Arial",30,"bold"))
        time.sleep(2)
        turtle.bye()

def forward1():
    t.forward(50)
    winner()
def forward2():
    t2.forward(50)
    winner()

t.width(4)
go(300,-250,t)
t.left(90)
t.forward(500)
go(-300,200)
t.right(90)
t.shape("turtle")
t.color("yellow")

t2.width(4)
go(-300,-200,t2)
t2.shape("turtle")
t2.color("magenta")

turtle.onkey(forward1,"Right")
turtle.onkey(forward2,"space")
turtle.listen()


