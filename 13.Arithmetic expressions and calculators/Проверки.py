LEFT_ASSOC = 0
RIGHT_ASSOC = 1


OPERATORS = {
    '+': (0, LEFT_ASSOC),
    '-': (0, LEFT_ASSOC),
    '*': (5, LEFT_ASSOC),
    '/': (5, LEFT_ASSOC),
    '%': (5, LEFT_ASSOC),
    '^': (10, RIGHT_ASSOC)
}


def isOperator(token):
    return token in OPERATORS.keys()

def isAssociative(token, assoc):
    if not isOperator(token):
        raise ValueError('Invalid token: %s' % token)
    return OPERATORS[token][1] == assoc

print(isAssociative(''1'', RIGHT_ASSOC))