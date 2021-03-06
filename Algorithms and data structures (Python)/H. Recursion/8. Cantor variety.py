# Нарисуйте Канторово множество. Канторово множество нулевого порядка - горизонтальный отрезок.
# Удалив среднюю треть получим множество первого порядка. Повторяя данную процедуру получим остальные множества.


import turtle

turtle.speed(0)
turtle.shape('turtle')
turtle.pensize(2)


def cantor_variety(l, n, x, y):
    if n == 0:
        return
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(l)
    y -= 20
    cantor_variety(l/3, n-1, x, y)
    cantor_variety(l/3, n-1, x+l*2/3, y)


cantor_variety(500, 6, -300, 200)
turtle.done()



# __________________________________________________________________________________


# import turtle
#
#
# turtle.shape('turtle')
# turtle.speed(0)
#
# def cantor_variety(x, y, l):
#     if l > 1:
#         turtle.penup()
#         turtle.goto(x, y)
#         turtle.pendown()
#         turtle.forward(l)
#         y -= 20
#         cantor_variety(x, y, l / 3)
#         cantor_variety(x + l * 2 / 3, y, l / 3)
#
# cantor_variety(-300, 200, 500)
# turtle.done()
