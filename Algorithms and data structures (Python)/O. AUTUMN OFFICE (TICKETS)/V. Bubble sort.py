# Сортировка методом пузырька

def bubble_sort(A):
    """Сортировка списка А методом пузырька"""
    n = len(A)
    for bypass in range(1, n):
        for k in range(0, n-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


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
    test_sort(bubble_sort)
