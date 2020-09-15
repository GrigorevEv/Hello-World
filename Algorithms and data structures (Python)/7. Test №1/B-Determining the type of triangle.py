# Определите тип треугольника (остроугольный, тупоугольный, прямоугольный) с данными сторонами.
# Формат входных данных
# Даны три натуральных числа – стороны треугольника. Каждое число вводится с новой строки.
# Формат выходных данных
# Необходимо вывести одно из слов: right для прямоугольного треугольника,
# acute для остроугольного треугольника, obtuse для тупоугольного треугольника или impossible,
# треугольника с такими сторонами не существует.

import math


def trangle():
    x = int(input())
    y = int(input())
    z = int(input())
    c = max(x, y, z)
    if c == x:
        a, b = y, z
    elif c == y:
        a, b = x, z
    else:
        a, b = x, y
    angle = math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
    if angle == 90:
        print('right')
    elif angle < 90:
        print('acute')
    elif 180 > angle > 90:
        print('obtuse')
    elif angle == 180:
        print('impossible')
    else:
        print('impossible')


trangle()
