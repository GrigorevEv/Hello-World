# Вклад в банке составляет x рублей.
# Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается.
# Каждый год сумма вклада становится больше.
# Надо определить, через сколько лет вклад составит не менее y рублей.
# Формат входных данных
# Три натуральных числа: x, p, y.
# Формат выходных данных
# Число лет, через сколько лет вклад составит не менее y рублей.


A = list(map(int, input().split()))
i = 0
while A[0] < A[2]:
    A[0] *= 1 + A[1]/100
    A[0] = int(A[0]*100)/100
    i += 1
print(i)
