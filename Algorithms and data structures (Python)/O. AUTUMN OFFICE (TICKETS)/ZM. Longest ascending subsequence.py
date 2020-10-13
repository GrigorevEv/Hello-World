# Наибольшая возрастающая подпоследовательность.


def las(a):
    f = [0] * (len(a))
    for i in range(len(a)):
        m = 0
        for j in range(0, i):
            if a[i] > a[j] and f[j] > m:
                m = f[j]
        f[i] = m + 1
    print(f)
    return max(f)


print(las([-1, 1, 2, 3, 4, 3, 2, 10]))
