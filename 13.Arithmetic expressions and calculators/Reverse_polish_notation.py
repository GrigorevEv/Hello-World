# https://ir.cwi.nl/pub/9251
# https: // en.wikipedia.org / wiki / Shunting - yard_algorithm
# https://commons.wikimedia.org/w/index.php?curid=10960619

#Associativity constants for operators
LEFT_ASSOC = 0
RIGHT_ASSOC = 1

#Supported operators(в качестве значений словарей - используются кортежи)
OPERATORS = {
    '+': (0, LEFT_ASSOC),
    '-': (0, LEFT_ASSOC),
    '*': (5, LEFT_ASSOC),
    '/': (5, LEFT_ASSOC),
    '%': (5, LEFT_ASSOC),
    '^': (10, RIGHT_ASSOC)
}

#Test if a certain token is operator(проверяет, является ли определенный токен оператором, возвращает булево значение)
def isOperator(token: bool):
    return token in OPERATORS.keys()


#Test the associativity type of a certain token (проверяет ассоциативность токена, сравнивая его с параметром assoc)
def isAssociative(token, assoc):
    if not isOperator(token):
        raise ValueError('Invalid token: %s' % token)
    return OPERATORS[token][1] == assoc

#Compare the precedence of two tokens (сравнивает приоритеты двух токенов)
def cmpPrecedence(token1, token2):
    if not isOperator(token1) or not isOperator(token2):
        raise ValueError('Invalid tokens: %s %s' % (token1, token2))
    return OPERATORS[token1][0] - OPERATORS[token2][0]

#Transforms an infix expression to RPN
def infixToRPN(tokens):
    out = []
    stack = []
    #For all the input tokens [S1] read the next token [S2]
    for token in tokens:
        if isOperator(token):
            # If token is an operator (x) [S3]
            while len(stack) != 0 and isOperator(stack[-1]):
                # [S4]
                if (isAssociative(token, LEFT_ASSOC) and cmpPrecedence(token, stack[-1]) <= 0) :
                # 1) Если ассоциативность токена равна LEFT_ASSOC(+,-,/,*) и приоритет данного и предыдущего токенов <=0,
                # т.е. это означает, например, что если данный токен + или -, а предыдущий *,/ или ^
                # (или данный токен *,/, а предыдущий ^), то кладем предыдущий - в стек out.
                # В противном случае помещаем его в стек stack, чтобы потом извлечь получив при этом правильный приоритет.
                    # [S5] [S6]
                    out.append(stack.pop())
                    continue
                break
            # [S7]
            stack.append(token)
        elif token == '(':
            stack.append(token) # [S8]
        elif token == ')':
            # [S9]
            while len(stack) != 0 and stack[-1] != '(':
                out.append(stack.pop()) # [S10]
                # Пока не дойдем до ( в стеке stack, переносим из stack в out токены
            stack.pop() # [S11] удаляем (
        else:
            out.append(token) # [S12]
    while len(stack) != 0:
        # [S13]
        out.append(stack.pop())
    return out

if __name__ == '__main__':
    print(infixToRPN(input()))