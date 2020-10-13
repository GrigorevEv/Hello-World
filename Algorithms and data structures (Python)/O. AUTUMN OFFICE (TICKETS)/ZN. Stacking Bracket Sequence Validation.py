import Stack_LIFO


# Написать программу, определяющую правильность введенного скобочного выражения
# , в котором используются скобки 3 видов: (), {}, /.

def is_braces_sequence_correct(s: str):
    """
    Проверяет корректность скобочной последовательности
    из круглых, квадратных, и наклонных скобок ()[]//

    >>> is_braces_sequence_correct('///')
    False
    >>> is_braces_sequence_correct('45')
    True
    >>> is_braces_sequence_correct('//[]')
    True
    >>> is_braces_sequence_correct('/(([()]))/[]//')
    True
    >>> is_braces_sequence_correct('/([])/[]')
    True
    >>> is_braces_sequence_correct('(](]')
    False
    >>> is_braces_sequence_correct('(')
    False
    >>> is_braces_sequence_correct('([[[]]])')
    True
    >>> is_braces_sequence_correct(']')
    False
    >>> is_braces_sequence_correct('/')
    False
    >>> is_braces_sequence_correct('(/)/')
    False
    """
    flag = True
    Stack_LIFO.clear()
    for brace in s:
        if brace not in '()[]/':
            continue
        if brace in '([' or flag is True and brace in '/':
            Stack_LIFO.push(brace)
            if brace in '/':
                flag = False
        else:
            if Stack_LIFO.is_empty():
                return False
            left = Stack_LIFO.pop()
            right = ''
            if left == '(':
                right = ')'
            elif left == '[':
                right = ']'
            elif left == '/':
                right = '/'
                flag = True
            if right != brace:
                return False
    return Stack_LIFO.is_empty()


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
