# Нарисуйте кривую дракона. Кривая дракона нулевого порядка - горизонтальный отрезок.
# Разделим отрезок пополам и построим на нем прямой угол, получив кривую дракона первого порядка:
# На сторонах прямого угла снова построим прямые углы.
# При этом вершина первого угла находится справа от начальной точки A,
# а направления, в которых строятся вершины остальных углов, чередуются.


import turtle


turtle.shape('turtle')
turtle.speed(0)
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()


def dragon_curve(length, depth, sign=1):
    if depth == 1:
        turtle.fd(length)
        return
    length = ((length ** 2) / 2) ** 0.5
    turtle.rt(45*sign)
    dragon_curve(length, depth - 1, 1)
    turtle.lt(90*sign)
    dragon_curve(length, depth - 1, -1)
    turtle.rt(45*sign)


dragon_curve(200, 9)
turtle.done()

