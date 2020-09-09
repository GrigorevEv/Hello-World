import turtle

turtle.shape('turtle')
n = 10
x = y = 0
for i in range(10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    n+=15
    x+=-7
    y+=-7

