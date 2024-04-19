i = 0
while i<10:
    print(i)
    i = i+1

for n in range (10):
    print(n)
    
colors = ["Yellow","Green"]

colors.append("Red")

for n in range (5):
    co = input("Enter color:")
    colors.append(co)

print(colors)

alphabets = ['b','c','m','w']

fruits = ["Apple"]

print (len(alphabets))

for t in range (len(alphabets)):
    s = str("Enter the name of a fruit that starts with "+alphabets[t]+": ")
    fr = input(s)
    fruits.append(fr)

print(fruits)

import turtle

t = turtle.Turtle()

for i in range(8):
    t.color(colors[i])
    t.width(5)
    t.forward(100)
    t.left(45)
