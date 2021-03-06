# Сдать решение задачи H-Числа в словарном порядке
# Напечатайте входную последовательность натуральных чисел, отсортировав ее по возрастанию сначала единиц, потом десятков, потом сотен и тп.
# Входные данные
# Целое число 0 < N ≤ 1000. Затем N натуральных чисел, не превышающих 30000, через пробел.
# Выходные данные
# Числа по возрастанию единиц, при равных единиц - по возрастанию десятков, при равных единицах и десятков - по возрастанию сотен и тп.


N = int(input())
s = list(map(int, input().split()))
s = sorted(s, key=lambda x: (x % 10, x % 100, x % 1000))
for i in range(len(s)):
    print(s[i], end=' ')


# https://webdevblog.ru/kak-ispolzovat-v-python-lyambda-funkcii/
# https://server.179.ru/tasks/python/theory/19-lambda.html
