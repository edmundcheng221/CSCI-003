"""
Homework #09
CSCI-UA 0003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-22
"""

import turtle
import math

t = turtle.Turtle()

dictions = [{"width": [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]},
                {"height": [100,120,140,160,180,200,220,240,260,280]},
                {"length": [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]},
                {"color": ["blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue"]}]

wn = turtle.Screen()


def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()


x = -300
y = -300
t.up()
t.goto(x, y)
t.down()
i = 0
for i in range(10):
    wid = dictions[0]['width'][i]
    hei = dictions[1]['height'][i]
    length = dictions[2]['length'][i]
    col = dictions[3]['color'][i]

    drawRectangle(t, wid, hei, col)
    drawTriangle(t, length, col)
    i += 1
    x += 70
    y += 70
    t.up()

    t.goto(x, y)
    t.down()


# The drawing is the boot of a knight with leg getting longer

wn.mainloop()  # keeps window open