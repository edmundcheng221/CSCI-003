"""
Homework #06
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-01

"""
import turtle

wn = turtle.Screen()


def line(t, coord1, coord2):
    wn = turtle.Screen()
    t.penup()
    t.goto((coord1[0], coord1[1]))
    t.pendown()
    t.goto((coord2[0], coord2[1]))
    # wn.mainloop()

#test
# line(turtle, [200, 100], [50, 150])


def poly(t, *coords):
    wn = turtle.Screen()
    t.penup()
    t.goto(coords[0])
    t.pendown()
    idx = 0
    while idx < len(coords) - 1:
        t.goto(coords[idx + 1])
        idx += 1

    t.goto(coords[0])
    # wn.mainloop()

#test
# poly(turtle, [50, 75], [25, 150], [10, 35], [100, 200], [20, 100])


def rectangle(t, coord, width, height, color):
    wn = turtle.Screen()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(coord)
    t.pendown()
    t.goto([coord[0] + width, coord[1]])
    t.goto([coord[0] + width, height + coord[1]])
    t.goto([coord[0], height + coord[1] ])
    t.goto(coord)
    t.end_fill()
    # wn.mainloop()

#test
# rectangle(turtle, [10, 50], 100, 70, "red")


if __name__ == '__main__':
    import turtle
    t = turtle.Turtle()
    wn = turtle.Screen()
    rectangle(t, [0, 0], 100, 200, 'green')
    t.color('blue')
    poly(t, [100, 100], [50, 50], [-50, 50])
    poly(t, [-100, 100], [-100, 50], [-200, 50], [-200, 100], [-150, 0])
    # poly(t, [0, 0], 100, 200)
    wn.mainloop()
