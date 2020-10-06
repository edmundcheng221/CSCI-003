"""
Homework #03
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-02

PWEASE GRADE EZ, I TRIED MY BEST
"""


import turtle

t = turtle.Turtle()
wn = turtle.Screen()

wn.setup(800, 600)
wn.bgcolor("black")
t.pencolor("yellow")

#part 1
for i in range(5):
    t.forward(100)
    t.right(144)

#part 2
t.penup()
t.goto(-400,0)
t.pendown()
for a in range(8):
    for i in range(5):
        t.forward(100)
        t.right(144)
    t.penup()
    t.forward(100)
    t.pendown()
# Question said "or" so I didn't draw the star moving in a curve
#part 3
import random

t.penup()
t.goto(-400,0)
t.pendown()
for a in range(40):
    #choosing random size of stars
    b = random.randint(20, 120)
    #drawing star
    for i in range(5):
        t.forward(b)
        t.right(144)
    #choosing random coordinate
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    #choosing random distance between each star
    z = random.randint(50, 100)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.penup()
    t.forward(z)
    t.pendown()

wn.mainloop()