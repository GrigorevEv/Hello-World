# Нарисуйте «бабочку» из окружностей.
# Используйте функцию, рисующую окружность.

import turtle


def infinity(k, d):
    """
    k - количество парных лепестков
    d - условный размер лепестка
    """
    turtle.shape('turtle')
    turtle.speed(500)
    turtle.left(90)
    n = 50
    e = 5
    for i in range(k):
        for j in range(n):
            turtle.forward(e)
            turtle.left(360/n)
        for k in range(n):
            turtle.forward(e)
            turtle.right(360/n)
        e += d


infinity(40, 1)
