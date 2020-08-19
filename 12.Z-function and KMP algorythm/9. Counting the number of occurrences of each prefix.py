# https://e-maxx.ru/algo/prefix_function


def p_func(s, t):
    n = len(s)
    m = len(t)
    pi = [0] * n
    k = 0
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    ans = [0] * n
    for i in range(n):
        ans[pi[i]] += 1
    print(ans)
    for i in range(n-1, 0, -1):
        ans[pi[i-1]] += ans[i]
    print(ans)

    return pi



print(p_func('abcdabcdababcd', 'abadfgabc'))
