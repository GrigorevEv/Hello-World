import turtle
import math

def polygon(n,a):
    '''n - количество углов многоугольника,
     a - длина стороны треугольника'''
    turtle.shape('turtle')
    if n >=3:
        for k in range(3, n + 1):
            r = math.radians(360 / (2 * k))
            f = a / (2 * math.sin(r))
            turtle.penup()
            turtle.goto(f, 0)
            turtle.pendown()
            turtle.left(180 - 90 * (k - 2) / k)
            for i in range(k):
                turtle.forward(a)
                turtle.left(360 / k)
            turtle.right(180 - 90 * (k - 2) / k)
            a = a + 2
    else:
        print('Введите число больше 2')
polygon(150,2)

