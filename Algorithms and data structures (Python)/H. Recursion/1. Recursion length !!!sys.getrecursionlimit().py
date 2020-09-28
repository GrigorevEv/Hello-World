# С помощью функции fac(n) определите текущую установленную глубину рекурсии и сравните ваш результат
# с возвращаемым значением функции sys.getrecursionlimit().
# Учтите, что sys.getrecursionlimit() возвращает максимальную глубину стека вызовов,
# а не максимальную глубину рекурсии для какой-либо функции.


import sys

i = 0


def fac(n):
    global i
    i += 1
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


print(fac(997))
print(i)
print(sys.getrecursionlimit())
