# https://ir.cwi.nl/pub/9251
# https: // en.wikipedia.org / wiki / Shunting - yard_algorithm
# https://commons.wikimedia.org/w/index.php?curid=10960619

# Associativity constants for operators
LEFT_ASSOC = 0
RIGHT_ASSOC = 1

# Supported operators(в качестве значений словарей - используются кортежи)
OPERATORS = {
    '+': (0, LEFT_ASSOC),
    '-': (0, LEFT_ASSOC),
    '*': (5, LEFT_ASSOC),
    '/': (5, LEFT_ASSOC),
    '%': (5, LEFT_ASSOC),
    '^': (10, RIGHT_ASSOC)
}


# Test if a certain token is operator(проверяет, является ли определенный токен оператором, возвращает булево значение)
def is_operator(token: bool):
    return token in OPERATORS.keys()


# Test the associativity type of a certain token (проверяет ассоциативность токена, сравнивая его с параметром assoc)
def is_associative(token, assoc):
    if not is_operator(token):
        raise ValueError('Invalid token: %s' % token)
    return OPERATORS[token][1] == assoc


# Compare the precedence of two tokens (сравнивает приоритеты двух токенов)
def cmp_precedence(token1, token2):
    if not is_operator(token1) or not is_operator(token2):
        raise ValueError('Invalid tokens: %s %s' % (token1, token2))
    return OPERATORS[token1][0] - OPERATORS[token2][0]


# Transforms an infix expression to RPN
def infix_to_rpn(tokens):
    out = []
    stack = []
    # For all the input tokens read the next token
    for token in tokens:
        if is_operator(token):
            # If token is an operator (x)
            while len(stack) != 0 and is_operator(stack[-1]):
                if is_associative(token, LEFT_ASSOC) and cmp_precedence(token, stack[-1]) <= 0:
                    # Если ассоциативность токена равна LEFT_ASSOC(+,-,/,*)
                    # и приоритет данного и предыдущего токенов <=0,
                    # т.е. это означает, например, что если данный токен + или -, а предыдущий *,/ или ^
                    # (или данный токен *,/, а предыдущий ^), то кладем предыдущий - в стек out.
                    # В противном случае помещаем его в стек stack,
                    # чтобы потом извлечь получив при этом правильный приоритет.
                    out.append(stack.pop())
                    continue
                break
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while len(stack) != 0 and stack[-1] != '(':
                out.append(stack.pop())
                # Пока не дойдем до ( в стеке stack, переносим из stack в out токены
            stack.pop()  # удаляем (
        else:
            out.append(token)
    while len(stack) != 0:
        out.append(stack.pop())
    return out


if __name__ == '__main__':
    print(infix_to_rpn(input()))
