# Генерация всех перестановок (рекурсивная)

def find(number, a):
    """Ищет x ы в а и возвращает True, если такой есть
    False, если такого нет"""
    for x in a:
        if number == x:
            return True
    return False


def generate_permutations(n: int, m: int = -1, prefix=None):
    """Генерация всех перестановок N чисел в M позициях,
    с префиксом prefix """
    m = n if m == -1 else m  # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if m == 0:
        print(*prefix)
        return
    for number in range(1, n+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(n, m-1, prefix)
        prefix.pop()


generate_permutations(3, 2)