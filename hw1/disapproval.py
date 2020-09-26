"""
Homework #01
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-09-14

"""

import turtle

# Some boiler plate code
pen = turtle.Turtle()
wn = turtle.Screen()
# Here is where I start to write the code

pen.forward(50)  #Left eyebrow
pen.left(135)
pen.forward(20)
pen.up() # move the pointer to coordinates (40,-5)
pen.goto(40,-5)
pen.down()
pen.circle(20) # draw eye with radius 20

pen.up()
pen.goto(27,-20) # move to (27,-20) and draw the pupil
pen.down()
pen.circle(2)


pen.up()
pen.goto(100,0) # translate pointer to (100,0)
pen.down()
pen.right(135)        # adjust the angle to which we are drawing
pen.forward(50)      # draw right eyebrow
pen.left(135)
pen.forward(20)

pen.up()
pen.goto(140,-5)            # translate to (140,-5)
pen.down()
pen.circle(20)       # draw right eye

pen.up()
pen.goto(127,-20) # translate to (127,-20)
pen.down()
pen.circle(2)         # draw pupil

pen.up()
pen.goto(55,-65)          # translate pointer to (55,-65)
pen.right(135)         # adjust angle to which we are drawing
pen.down()
pen.forward(40)                     # draw mouth


# Rest of the boiler plate code
wn.mainloop() # keeps window open

