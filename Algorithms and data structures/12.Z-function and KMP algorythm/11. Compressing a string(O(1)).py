# https://e-maxx.ru/algo/prefix_function


def p_func(s):
    global t
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    print(pi)
    k = n - pi[n-1]
    if n % k == 0:
        t = s[0:k]
    return t



print(p_func('ababab'))
