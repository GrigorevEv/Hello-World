# https://e-maxx.ru/algo/z_function
# Пусть даны две строки.
# Найти все вхождения второй строки в первую.


def z_func(s):
    n = len(s)
    k = 0
    z = [0] * len(s)
    for i in range(0, n):
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1





z_func('abaaaba')
