# Поиск местоположения максимума в последовательности за один проход.

"""
>>> max_finding([1, 2, 44, 2, 4, 5])
2
"""


def max_finding(x: list):
    maximum = 0
    k = 0
    for i in range(len(x)):
        if x[i] > maximum:
            maximum = x[i]
            k = i
    return k

