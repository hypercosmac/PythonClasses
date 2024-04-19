import turtle

turtle.speed(speed="fastest")

t = turtle.Turtle()

scale = 0.3

turtle.bgcolor("skyblue")

def cir(col,rad):
    t.color(col)
    t.begin_fill()
    t.circle(scale*rad)
    t.end_fill()

def go(x,y,offset):
    t.penup()
    offx = 60*offset+scale*x
    t.goto(offx,scale*y)
    t.pendown()

for i in range(-5,5):
    #Ears
    go(-70,180,i)
    cir("black",30)
    go(70,180,i)
    cir("black",30)

    #Face
    go(0,70,i)
    cir("white",80)

    #Eyes
    go(-36,150,i)
    cir("black",16)
    go(36,150,i)
    cir("black",16)
    go(-36,154,i)
    cir("white",8)
    go(36,154,i)
    cir("white",8)

    #Nose
    go(0,110,i)
    cir("black",10)

    #Mouth
    t.right(90)
    t.circle(scale*10,180)
    go(0,110,i)
    t.circle(scale*10,-180)
    t.left(90)


t.hideturtle()
