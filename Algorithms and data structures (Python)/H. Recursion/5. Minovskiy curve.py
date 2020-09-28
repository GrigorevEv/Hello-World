# Нарисуйте кривую Минковского. Кривая Минковского нулевого порядка - горизонтальный отрезок.
# Затем на каждом шаге каждый из отрезков заменяется на ломанную, состоящую из 8 звеньев


import turtle

turtle.shape('turtle')
turtle.speed('fastest')
turtle.penup()
turtle.goto(-400, 100)
turtle.pendown()


def minovskiy_curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 4
    minovskiy_curve(l, n - 1)
    turtle.left(90)
    minovskiy_curve(l, n - 1)
    turtle.right(90)
    minovskiy_curve(l, n - 1)
    turtle.right(90)
    minovskiy_curve(l, n - 1)
    minovskiy_curve(l, n - 1)
    turtle.left(90)
    minovskiy_curve(l, n - 1)
    turtle.left(90)
    minovskiy_curve(l, n - 1)
    turtle.right(90)
    minovskiy_curve(l, n - 1)


minovskiy_curve(800, 4)



