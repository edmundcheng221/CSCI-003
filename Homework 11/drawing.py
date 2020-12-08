"""
Homework #11
CSCI-UA. 0003-001 Fall 2020
Edmund Cheng
ec3219
2020-12-06
"""

import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.tracer(0)
"""
# part 1
def draw(size):
    t.forward(size)

# part 2
def draw(size):
    t.forward(size / 3)
    t.left(60)
    t.forward(size / 3)
    t.right(120)
    t.forward(size / 3)
    t.left(60)
    t.forward(size / 3)

# part 3
def inner_draw(size):
    t.forward(size / 3)
    t.left(60)
    t.forward(size / 3)
    t.right(120)
    t.forward(size / 3)
    t.left(60)
    t.forward(size / 3)

def draw(size):
    inner_draw(size / 3)
    t.left(60)
    inner_draw(size / 3)
    t.right(120)
    inner_draw(size / 3)
    t.left(60)
    inner_draw(size / 3)

# part 4
def inner_inner_draw(size):
    t.forward(size / 3)
    t.left(60)
    t.forward(size / 3)
    t.right(120)
    t.forward(size / 3)
    t.left(60)
    t.forward(size / 3)

def inner_draw(size):
    inner_inner_draw(size / 3)
    t.left(60)
    inner_inner_draw(size / 3)
    t.right(120)
    inner_inner_draw(size / 3)
    t.left(60)
    inner_inner_draw(size / 3)

def draw(size):
    inner_draw(size / 3)
    t.left(60)
    inner_draw(size / 3)
    t.right(120)
    inner_draw(size / 3)
    t.left(60)
    inner_draw(size / 3)

# part 5
def draw(size):
    if size < 10:
        t.forward(size / 3)
        t.left(60)
        t.forward(size / 3)
        t.right(120)
        t.forward(size / 3)
        t.left(60)
        t.forward(size / 3)
    else:
        draw(size / 3)
        t.left(60)
        draw(size / 3)
        t.right(120)
        draw(size / 3)
        t.left(60)
        draw(size / 3)

# part 6
def draw(size, counter):
    counter -= 1
    if counter == -1:
        t.forward(size / 3)
        t.left(60)
        t.forward(size / 3)
        t.right(120)
        t.forward(size / 3)
        t.left(60)
        t.forward(size / 3)
    else:
        draw(size / 3, counter)
        t.left(60)
        draw(size / 3, counter)
        t.right(120)
        draw(size / 3, counter)
        t.left(60)
        draw(size / 3, counter)
"""


# part 7
def draw(size, counter):
    counter -= 1
    if counter == -1:
        t.forward(size / 3)
    else:
        draw(size / 3, counter)
        t.left(60)
        draw(size / 3, counter)
        t.right(120)
        draw(size / 3, counter)
        t.left(60)
        draw(size / 3, counter)


t.penup()
t.goto(-175 / 2, 175 / 2)
t.pendown()
for _ in range(3):
    draw(500, 4)
    t.right(120)

wn.update()
wn.mainloop()


