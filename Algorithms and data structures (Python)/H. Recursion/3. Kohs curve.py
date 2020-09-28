# Нарисуйте кривую Коха. Процесс её построения выглядит следующим образом:
# берём единичный отрезок, разделяем на три равные части и заменяем средний интервал равносторонним
# треугольником без этого сегмента. В результате образуется ломаная, состоящая из четырёх звеньев длины 1/3.
# На следующем шаге повторяем операцию для каждого из четырёх получившихся звеньев и т. д…
# Предельная кривая и есть кривая Коха.


import turtle

turtle.shape('turtle')
turtle.speed('fastest')
turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()


def koch_line(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 3
    koch_line(l, n - 1)
    turtle.left(60)
    koch_line(l, n - 1)
    turtle.right(120)
    koch_line(l, n - 1)
    turtle.left(60)
    koch_line(l, n - 1)


koch_line(800, 5)
