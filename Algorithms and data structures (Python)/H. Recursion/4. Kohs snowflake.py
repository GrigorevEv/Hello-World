# Три копии кривой Коха, построенные (остриями наружу) на сторонах правильного треугольника,
# образуют замкнутую кривую бесконечной длины, называемую снежинкой Коха


import turtle

turtle.shape('turtle')
turtle.speed('fastest')
turtle.penup()
turtle.goto(-300, 100)
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


def koch_snowflake(l, n):
    koch_line(l, n)
    turtle.right(120)
    koch_line(l, n)
    turtle.right(120)
    koch_line(l, n)


koch_snowflake(500, 3)
