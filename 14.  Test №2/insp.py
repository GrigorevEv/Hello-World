def p_func(t, s):
    st = s + '#' + t
    n = len(st)
    p = len(s)
    pi = [0] * n
    k = 0
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and st[i] != st[j]:
            j = pi[j-1]
        if st[i] == st[j]:
            j += 1
            pi[i] = j
    for i in range(p+1, n):
        if pi[i] == p:
            k += 1
    return k

string = 'abaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabayabaxabayabazabay'
occurrences = []

for i in range(1, len(string)):
    if string.count(string[0:i]) + string.count(string[0:i], 1) >= 3:
        occurrences.append(len(string[0:i]))
print(occurrences)



