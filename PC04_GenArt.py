# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:05:26 2021

@author: Grant Young
"""

import turtle, random
turtle.colormode(255)
panel=turtle.Screen()
w=750
h=750
panel.setup(width=w,height=h)

turtle1=turtle.Turtle()
turtle1.down()
for hatching in range(50):
    turtle1.up()
    turtle1.goto(0,0)
    turtle1.down()
    turtle1.pensize(random.randint(1,5))
    turtle1.right(random.randint(0,360))
    turtle1.forward(550)

turtle2=turtle.Turtle()
ichi=((98, 60, 234),(231, 223, 198),(233, 241, 247),(84, 66, 107),(219, 213, 178))
ni=((246, 254, 219),(230, 211, 163),(216, 209, 116),(182, 196, 84),(145, 151, 42))
san=((234, 99, 140),(179, 60, 134),(25, 14, 79),(3, 1, 44),(0, 42, 34))
shi=(ichi,ni,san)

turtle2.up()
turtle2.goto(-225,150)
turtle2.down()
for multirow in range(10):
    for singlerow in range(15):
        turtle2.color(random.choice(random.choice(shi)))
        turtle2.begin_fill()
        for blok in range(4):
            turtle2.forward(30)
            turtle2.left(90)
        turtle2.end_fill()
        turtle2.up()
        turtle2.forward(30)
        turtle2.down()
    turtle2.up()
    turtle2.right(90)
    turtle2.forward(30)
    turtle2.right(90)
    turtle2.forward(450)
    turtle2.right(180)
    turtle2.down()
turtle2.up()

turtle.done()
