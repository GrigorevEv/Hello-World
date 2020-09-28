# Нарисуйте кривую Леви. Она получается, если взять половину квадрата вида /\,
# а затем каждую сторону заменить таким же фрагментом и так далее.


import turtle


turtle.shape('turtle')
turtle.speed('fastest')
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()


def levi_curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l = ((l**2)/2)**0.5
    turtle.left(45)
    levi_curve(l, n - 1)
    turtle.right(90)
    levi_curve(l, n - 1)
    turtle.left(45)


levi_curve(200, 9)
