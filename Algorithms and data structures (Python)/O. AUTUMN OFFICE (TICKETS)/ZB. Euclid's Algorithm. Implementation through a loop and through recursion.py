# Алгоритм Евклида. Реализация через цикл и через рекурсию

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


c = int(input())
d = int(input())
print(gcd(c, d))