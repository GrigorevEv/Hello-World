# https://e-maxx.ru/algo/prefix_function


def p_func(s):
    n = len(s)
    pi = [0] * n
    t = []
    k = 0
    for f in range(n):
        t += s[f]
        rt = t[::-1]
        for i in range(1, len(rt)):
            j = pi[i-1]
            while j > 0 and rt[i] != rt[j]:
                j = pi[j-1]
            if rt[i] == rt[j]:
                j += 1
                pi[i] = j
        k += len(rt) - max(pi)
    return k


print(p_func('abc'))
