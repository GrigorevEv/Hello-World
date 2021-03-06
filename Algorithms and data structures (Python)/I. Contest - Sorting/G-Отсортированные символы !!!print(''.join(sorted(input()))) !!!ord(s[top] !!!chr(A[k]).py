# Сдать решение задачи G-Отсортированные символы
# Напечатайте входную строку, отсортировав ее по возрастанию ASCII кода символов.
# Входные данные
# Строка, заканчивающаяся точкой, длиной не более 1000 символов. Точку сортировать не нужно.
# Все, что находится после первой точки - игнорировать.
# Выходные данные
# Отсортированная строка с точкой на конце.

########################################################

# print(''.join(sorted(input())))

########################################################

s = input()
A = []
top = 0
# Добавление в массив x каждого элемента из строки str,с конвертацией каждого значения символа в int
while top < len(s):
    if s[top] == '.':
        break
    A.append(ord(s[top]))
    top += 1


def sort(x):
    """
    Cортировка Тони Хоара(quick sort)
    """
    if len(x) <= 1:
        return
    barrier = x[0]
    left, middle, right = [], [], []
    for g in x:
        if g < barrier:
            left.append(g)
        elif g == barrier:
            middle.append(g)
        else:
            right.append(g)
    sort(left)
    sort(right)
    i = 0
    for g in left + middle + right:
        x[i] = g
        i += 1


sort(A)  # Сортировка массива x значений элементов по возрастанию
for k in range(len(A)):  # конвертация в char и вывод обратно в cтроку.
    print(chr(A[k]), end='')
print('.', end='')
