# Поиск максимума и подсчёт количества элементов, равных максимальному.
"""
>>> max_finding([1, 2, 44, 2, 4, 5])
44
>>> find_count_elemets_eq_max([1, 2, 33, 4, 33, 9, 33])
3
"""


def max_finding(x: list):
    maximum = 0
    for i in range(len(x)):
        if x[i] > maximum:
            maximum = x[i]
    return maximum


def find_count_elemets_eq_max(x: list):
    maximum = 0
    k = 0
    for i in range(len(x)):
        if x[i] > maximum:
            maximum = x[i]
            k = 1
        elif x[i] == maximum:
            k += 1
    return k

