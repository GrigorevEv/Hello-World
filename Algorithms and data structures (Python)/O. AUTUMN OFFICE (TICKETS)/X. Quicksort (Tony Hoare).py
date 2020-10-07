# Сортировка Тони Хоара или быстрая сортировка

def q_sort(a):
    if len(a) <= 1:
        return
    barrier = a[0]
    l, m, r = [], [], []
    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
        k = 0
        q_sort(l)
        q_sort(r)
        for i in l + m + r:
            a[k] = i
            k += 1
        return a


print(q_sort([5, 4, 3, 2, 1, 0]))
