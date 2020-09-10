# Нарисуйте «цветок» из окружностей.
# Используйте функцию, рисующую окружность.

import turtle


def flower(k, s):
    """
    k - количество парных лепестков
    s - условный размер лепестка
    """
    turtle.shape('turtle')
    turtle.speed(500)
    n = 100
    for i in range(k):
        for j in range(n):
            turtle.forward(s)
            turtle.left(360/n)
        for f in range(n):
            turtle.forward(s)
            turtle.right(360/n)
        turtle.right(-360/k)


flower(40, 7)
