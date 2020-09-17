# Хорошим примером для иллюстрации рекурсивных алгоритмов являются задачи рисования фракталов.
# Фрактальные кривые, обладающие бесконечным самоподобием, не являются спрямляемыми:
# хоть их и можно изобразить на плоскости конечной площади, эти кривые имют бесконечную длину.
# Соответственно, программно их невозможно нарисовать полностью: всегда будет возможность нарисовать кривую детальнее.
# Поэтому, фрактальные кривые рисуют в некотором приближении, заранее фиксируя максимально допустимую глубину рекурсии.
# Пример программы, использующей рекурсивные вызовы функции, чтобы нарисовать ветку:


import turtle

turtle.speed(0)


def draw(l, n):
    if n == 0:
        turtle.left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(l)


draw(400, 5)
