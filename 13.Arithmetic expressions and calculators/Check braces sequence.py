import Stack_LIFO

def is_braces_sequence_correct(s: str):
    """
    Проверяет корректность скобочной последовательности
    из круглых и квадратных скобок ()[]
    >>> is_braces_sequence_correct('(([()]))[]')
    True
    >>> is_braces_sequence_correct('(](]')
    False
    >>> is_braces_sequence_correct('(')
    False
    >>> is_braces_sequence_correct(']')
    False
    """
    for brace in s:
        if brace in '()[]':
            continue
        if brace in '([':
            Stack_LIFO.push(brace)
        else:
            assert brace in ')]', 'Ожидалась закрывающая скобка: ' + str(brace)
            if Stack_LIFO.is_empty():
                return False
            left = Stack_LIFO.pop()
            assert left in '([', 'Ожидалась открывающая скобка: ' + str(brace)
            if left == '(':
                right = ')'
            elif left == '[':
                right = ']'
            if right != brace:
                return False
    return Stack_LIFO.is_empty()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

