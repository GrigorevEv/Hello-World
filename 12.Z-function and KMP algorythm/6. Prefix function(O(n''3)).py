# https://e-maxx.ru/algo/prefix_function


def p_func(s):
    n = len(s)
    pi = [0] * n
    for i in range(n):
        for k in range(1, i + 1):
            equal = True
            for j in range(k):
                if s[j] != s[i - k + 1 + j]:
                    equal = False
                    break
            if equal:
                pi[i] = k
    return pi


print(p_func('abcabcd'))
