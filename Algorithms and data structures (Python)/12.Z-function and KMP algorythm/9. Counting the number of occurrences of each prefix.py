# https://e-maxx.ru/algo/prefix_function


def p_func(s, t):
    # В первом варианте требуется для каждого префикса s[0 ... i] посчитать,
    # сколько раз он встречается в самой же строке s
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    ans1 = [0] * n
    for i in range(n):
        ans1[pi[i]] += 1
    for i in range(n-1, 0, -1):
        ans1[pi[i-1]] += ans1[i]
    # Во втором варианте задачи дана другая строка t,
    # и требуется для каждого префикса s[0 ... i] посчитать,
    # сколько раз он встречается в t.
    st = s + '#' + t
    m = len(st)
    pi = [0] * m
    for i in range(1, m):
        j = pi[i-1]
        while j > 0 and st[i] != st[j]:
            j = pi[j-1]
        if st[i] == st[j]:
            j += 1
            pi[i] = j
    ans2 = [0] * (len(t) + 1)
    for i in range(n, m):
        ans2[pi[i]] += 1
    for i in range(len(ans2) - 1, 0, -1):
        ans2[pi[i-1]] += ans2[i]

    return ans1[1::], ans2[1::]


print(p_func('abcdabcdababcd', 'abcdabcdababcdaaaababab'))
