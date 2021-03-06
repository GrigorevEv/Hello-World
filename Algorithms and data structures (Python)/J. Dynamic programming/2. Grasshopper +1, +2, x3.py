# Упражнение №2
# Решите задачу о количестве способов достичь точки n из точки 1, если кузнечик умеет прыгать +1, +2 и *3.
# Кузнечик стоит на позиции 1 (не 0)


def grasshopper(n):
    f = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        if i % 3 == 0:
            f[i] = f[i-1] + f[i - 2] + f[i//3]
        else:
            f[i] = f[i - 1] + f[i - 2]
    return f[n]


print(grasshopper(6))
