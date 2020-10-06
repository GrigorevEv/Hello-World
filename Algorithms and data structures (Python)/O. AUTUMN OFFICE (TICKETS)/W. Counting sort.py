# Сортировка подсчетом

def counting_sort(a: list):
    f = [0]*10
    n = len(a)
    m = len(f)
    for i in range(n):
        f[a[i]] += 1
    for digit in range(m):
        print(str(digit)*f[digit], end='')


counting_sort([5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 9, 2, 8, 4, 6, 6, 5])
