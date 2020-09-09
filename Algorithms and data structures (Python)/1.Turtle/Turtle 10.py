import turtle
import math
import  time
def star(n,a):
    '''n - количество углов звезды,
     a - длина линий'''
    turtle.shape('turtle')
    turtle.left(180)
    if n>=5:
        if n%2==0:
            for i in range(n):
                turtle.forward(a)
                turtle.right(180)
                turtle.right((180*(n-2) / (3*n)))
        else:
            for i in range(n):
                turtle.forward(a)
                turtle.left(180-180*(n-2) / (3*n))
    else:
        print('Введите число больше 2')
star(5,200)
turtle.penup()
turtle.goto(90,-65)
turtle.pendown()
star(11,200)
time.sleep(5)

