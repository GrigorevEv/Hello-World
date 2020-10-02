# Проверка последовательности чисел на наличие элемента с заданными свойствами
# и на соответствие всех элементов заданному свойству.

'''
>>> even_digits_in_sequence([1, 2, 4, 6, 3])
2 4 6
>>> even_digits_in_sequence([1, 3, 5])
0
>>> all_digits_in_sequence_are_even([2, 4, 6, 122, 1000000])
True
>>> all_digits_in_sequence_are_even([2, 4, 5, 122, 1000000])
False
'''


def even_digits_in_sequence(x: list):
    for i in range(len(x)):
        if x[i] % 2 == 0:
            print(x[i], end=' ')


def all_digits_in_sequence_are_even(x: list):
    for i in range(len(x)):
        if x[i] % 2 != 0:
            print(False)
            break
    else:
        print(True)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

