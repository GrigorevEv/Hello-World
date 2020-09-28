import Reverse_polish_notation

def stack_calculator(tokens):
    """Калькулятор, который считает выражения в обратной польской нотации
    >>> stack_calculator('(1+2^3)*2')
    18
    >>> stack_calculator('(1+2*2+3^2)^(1*2+1)')
    2744
    >>> stack_calculator('1+2+3-1-2+9^2')
    84
    >>> stack_calculator('5-1-2+5')
    7
    >>> stack_calculator('5-5')
    0
    """
    tokens = (Reverse_polish_notation.infix_to_rpn(tokens))
    stack = []
    for token in tokens:
        if token in '0123456789':
            stack.append(int(token))
        else:
            x = stack.pop()
            y = stack.pop()
            if token == '+':
                z = y + x
            elif token == '-':
                z = y - x
            elif token == '*':
                z = y * x
            elif token == '/':
                z = y / x
            elif token == '^':
                z = y ** x
            stack.append(z)
    return stack[0]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
