import turtle
import time
import random

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

turtle.bgcolor("skyblue")
t = turtle.Turtle()
t.hideturtle()
fontoption = ("Verdana",30,"bold")
operations = ["+","-","*"]
colors = ["Orange","blue","yellow","purple","violet"]
points = 0
highest = int(turtle.textinput("Setup","Enter highest number to operate"))
while True:
    go(100,300)
    t.write("Points: "+str(points),font=fontoption)
    go(-80,0)
    num1 = random.randint(2,highest)
    num2 = random.randint(2,highest)
    if num2>num1:
        temp = num1
        num1 = num2
        num2 = temp
    oper = random.choice(operations)
    if oper == "+":
        answer = str(num1+num2)
    elif oper == "-":
        answer = str(num1-num2)
    elif oper == "*":
        answer = str(num1*num2)
    problem = str(num1)+oper+str(num2)
    t.color(random.choice(colors))
    t.write(problem,font=("Verdana",50,"bold"))
    response = turtle.textinput("Math Problem","Enter your answer")
    go(-65,-50)
    if response == answer:
        t.color("green")
        t.write("Correct!",font=fontoption)
        points = points + 1
    else:
        t.color("Red")
        t.write("Incorrect",font=fontoption)
        points = points - 1
    time.sleep(2)
    t.clear()
