# Проверка упорядоченности массива за O(N)

def check_sorted(a, ascending=True):
    """Проверка отсортированности за O(len(a))"""
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, len(a)-1):
        if s * a[i] > s * a[i+1]:
            flag = False
            break
    return flag


print(check_sorted([5, 4, 3, 2, 1, 0], ascending=False))
