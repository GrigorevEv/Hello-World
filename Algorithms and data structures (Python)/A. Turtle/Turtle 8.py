# Нарисуйте пружину.
# Используйте функцию, рисующую дугу.

import turtle


def spring(k):
    """
    Функция для рисования пружины.
    k - количество витков
    """
    turtle.shape('turtle')
    turtle.speed(500)
    turtle.left(90)
    n = 50
    e = 5
    f = 1
    for i in range(k):
        for j in range(n):
            turtle.forward(e)
            turtle.right(180/n)
        for k in range(n):
            turtle.forward(f)
            turtle.right(180/n)


spring(5)
