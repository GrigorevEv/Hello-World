# Упражнение №4
# Модифицируйте алгоритм вычисления значений целевой функции так,
# чтобы вычислить значения prev[i], и восстановите траекторию наименьшей стоимости из точки 1 в точку n.

def count_min_cost(n, price: list):
    c = [0, price[1], price[2]]+[0]*(n-2)
    for i in range(3, n+1):
        c[i] = price[i] + min(c[i-1], c[i-2])
    prev = [n]
    i = n
    while i > 0:
        if c[i - 1] < c[i - 2]:
            i -= 1
        else:
            i -= 2
        prev.append(i)
    print(c[n])
    print(prev[::-1])


count_min_cost(11, [0, 2, 1, 20, 21, 10, 31, 17, 5, 16, 2, 25])
