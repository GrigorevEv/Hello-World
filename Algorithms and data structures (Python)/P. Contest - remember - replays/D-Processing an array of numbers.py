# На вход программа получает набор чисел, заканчивающихся решеткой.
# Вам требуется найти: среднее, максимальное и минимальное число в последовательности.
# Так же нужно вывести cумму остатков от деления суммы троек на последнее число тройки
# (каждые 3 введеных числа образуют тройку).
# Для понимания рассмотрим пример входных данных: 1 2 3 4 5 6 среднее: (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3.5
# максимум: 6 минимум: 1 сумма остатков троек: (1 + 2 + 3) mod 3 + (4 + 5 + 6) mod 6 = 6 mod 3 + 15 mod 6 = 0 + 3 = 3
# Среднее выводить, округлив до трех знаков после запятой. Для этого нужно использовать функцию round(x, 3)
# Того ваша программа должна вывести: 3.5 6 1 3
# Подумайте, имеет ли смысл хранить всю последовательность.
# Формат входных данных
# Последовательность чисел, заканчивающися '#'. Все числа от 1 до 100.
# Количество чисел в последовательности кратно трем. Одно число на строку.
# Формат выходных данных
# Четыре числа, разделенных пробелом.

a = []
digit = 0
while digit != '#':
    digit = input()
    a.append(int(digit))
