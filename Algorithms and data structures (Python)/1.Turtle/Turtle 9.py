import turtle
import time

turtle.shape('turtle')
def circle(d,c,x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('black', c)
    turtle.begin_fill()
    turtle.circle(d)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def arc(d,c,x,y):
    turtle.width(8)
    turtle.color(c)
    turtle.right(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(1,51):
        turtle.forward(d)
        turtle.right(3.6)


def line (l,c,angle,x,y):
    turtle.width(8)
    turtle.color(c)
    turtle.right(angle)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(l)

circle(150,'yellow',0,0)
circle(25,'blue',-65,180)
circle(25,'blue',65,180)
line(50,'green',90,0,150)
arc(5,'red',77,100)
time.sleep(5)


