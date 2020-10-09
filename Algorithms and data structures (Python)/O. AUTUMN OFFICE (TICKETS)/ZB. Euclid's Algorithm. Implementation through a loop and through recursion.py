# Алгоритм Евклида. Реализация через цикл и через рекурсию

def gcd_recursion(a=int(input()), b=int(input())):
    if b == 0:
        return a
    else:
        return gcd_recursion(b, a % b)


print(gcd_recursion())


def gcd_cycle(a=int(input()), b=int(input())):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b


print(gcd_cycle())
