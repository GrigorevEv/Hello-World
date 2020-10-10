# Рекурсивная генерация всех чисел длины M


def generate_numbers(n: int, m: int, prefix=None):
    """Генерирует все числа (с лидирующими незначащими нулями)
    в N-ричной системе исчисления (N <= 10) длины M"""
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m-1, prefix)
        prefix.pop()


generate_numbers(2, 3)
