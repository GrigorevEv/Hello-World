import Reverse_polish_notation

def stack_calculator():
    tokens = (Reverse_polish_notation.infixToRPN(input()))
    stack = []
    for token in tokens:
        if token in '0123456789':
            stack.append(int(token))
        else:
            x = stack.pop()
            y = stack.pop()
            if token == '+':
                z = x + y
            elif token == '-':
                z = x - y
            elif token == '*':
                z = x * y
            elif token == '/':
                z = x / y
            elif token == '^':
                z = x ^ y
            stack.append(z)
    return stack[0]

print(stack_calculator())