# https://e-maxx.ru/algo/z_function
# Пусть даны две строки.
# Найти все вхождения второй строки в первую.


def z_func(t, p):
    s = p + '#' + t
    n = len(s)
    k = 0
    z = [0] * len(s)
    l, r = 0, 0  # координаты самого правого отрезка совпадения
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:   # i > r — т.е. текущая позиция лежит за пределами того, что мы уже успели обработать.
            z[i] += 1
        if i + z[i] - 1 > r:  # здесь выполняется обновление текущего самого правого отрезка совпадения [l;r]
            l = i
            r = i + z[i] - 1
    for i in range(n):
        if z[i] == len(p):
            k += 1
    print(k, 'вхожд.')


z_func('abaaaba', 'aba')
