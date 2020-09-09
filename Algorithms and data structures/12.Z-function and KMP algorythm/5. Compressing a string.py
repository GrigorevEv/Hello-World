# https://e-maxx.ru/algo/z_function


def z_func(s):
    global t
    n = len(s)
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
        if i + z[i] == n and n % z[i] == 0:
            t = s[i::]
    return t


print(z_func('aabaabaabaabaabaab'))
