# Нахождение трёх максимальных элементов в последовательности за один проход.
"""
>>> three_max_elements([1, 2, 5, 6, 3, 4, 7, 8, 9])
7 8 9
>>> three_max_elements([1, 2, 7, 6, 3, 4, 7, 0, 9])
7 7 9
"""


def three_max_elements(x: list):
    a = b = c = 0
    for i in range(len(x)):
        if x[i] >= a:
            a, b, c = x[i], a, b
    print(c, b, a, end='')

