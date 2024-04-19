import turtle

t = turtle.Turtle()

t.color("red")

#Drawing the square
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

#Moving to start drawing the triangle
t.penup()
t.goto(100,100) #Top right corner
t.pendown()

#Drawing the triangle
t.color("yellow")
t.right(135)
t.forward(71)
t.left(90)
t.forward(71)

#Move to start drawing the door
t.penup()
t.goto(35,0)
t.pendown()

#Drawing the door
t.color("brown")
t.begin_fill()
t.right(90+45)
t.forward(40)
t.right(90)
t.forward(30)
t.right(90)
t.forward(40)
t.end_fill()

