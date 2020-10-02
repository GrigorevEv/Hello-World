# Однопроходные алгоритмы обработки последовательности: подсчёт, сумма, произведение
"""
>>> count_all_elements([1, 2, 3, 4, 5])
5
>>> sum_all_elements([1, 2, 3, 4, 5])
15
>>> mult_all_elements([1, 2, 3, 4, 5])
120
"""


def count_all_elements(x: list):
    k = 0
    for i in range(len(x)):
        k += 1
    return k


def sum_all_elements(x: list):
    k = 0
    for i in range(len(x)):
        k += x[i]
    return k


def mult_all_elements(x: list):
    k = 1
    for i in range(len(x)):
        k *= x[i]
    return k


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

