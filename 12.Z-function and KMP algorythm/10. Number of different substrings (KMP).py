# https://e-maxx.ru/algo/prefix_function


def p_func(s):
    n = len(s)
    pi = [0] * n
    k = 0
    t = ''
    for i in range(1, n):
        t += s[i]
        rt = t[::-1]
        j = pi[i-1]
        while j > 0 and rt[i] != rt[j]:
            j = pi[j-1]
        if rt[i] == rt[j]:
            j += 1
            pi[i] = j
        k += len(rt) + 1 - max(pi)
    print(k)


p_func('abc')
