# Алгоритм циклического сдвига в массиве. Реализация циклом, без срезов.

def cyclic_shift_l_r(a: list):
    tmp = a[0]
    for k in range(len(a)-1):
        a[k] = a[k+1]
    a[len(a)-1] = tmp
    return a


def cyclic_shift_r_l(a: list):
    tmp = a[len(a)-1]
    for k in range(len(a)-2, -1, -1):
        a[k+1] = a[k]
    a[0] = tmp
    return a


print(cyclic_shift_l_r([1, 2, 3, 4, 5]))
print(cyclic_shift_r_l([1, 2, 3, 4, 5]))
