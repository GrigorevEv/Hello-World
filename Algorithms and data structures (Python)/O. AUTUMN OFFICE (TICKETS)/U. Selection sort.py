# Сортировка выбором

def selection_sort(A):
    """Сортировка списка А выбором"""
    n = len(A)
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def test_sort(sort_algorithm):
    print('Тестируем: ', sort_algorithm.__doc__)
    print('testcase #1:', end='')
    a = [4, 5, 2, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print('Ok' if a == a_sorted else 'Fail')

    print('testcase #1:', end='')
    a = list(range(10, 20)) + list(range(0, 10))
    a_sorted = list(range(20))
    sort_algorithm(a)
    print('Ok' if a == a_sorted else 'Fail')

    print('testcase #1:', end='')
    a = [4, 2, 4, 2, 1]
    a_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(a)
    print('Ok' if a == a_sorted else 'Fail')


if __name__ == '__main__':
    test_sort(selection_sort)
