# https://e-maxx.ru/algo/z_function
# Дана строка s длины n.
# Требуется посчитать количество её различных подстрок.


def z_func(s):
    n = len(s)
    k = 0
    z = [0] * len(s)
    t = ''
    for i in range(0, n):
        t += s[i]
        rt = t[::-1]
        for j in range(1, len(rt)):
            while j + z[j] < len(rt) and rt[z[j]] == rt[j + z[j]]:
                z[j] += 1
        k += len(rt) - max(z)
    print(k)





z_func('fdgdflkdf;lkgkgkljdkljgdflkjlkdjfglkjdflkjgdlkllkghlk')
