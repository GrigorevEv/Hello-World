# Больше-меньше
# Вам дано выражение вида "a x b", где a и b - натуральные числа,
# а x - знак сравнения, '<' или '>'. Истинно ли данное выражение?
# Формат входных данных
# В первой строке число a, во второй знак сравнения, в третьей - число b. Оба числа - натуральные.
# Формат выходных данных
# Если выражение истинно, выведите YES, иначе NO

a = int(input())
x = input()
b = int(input())
if x == '>':
    if a > b:
        print('YES')
    else:
        print('NO')
else:
    if a < b:
        print('YES')
    else:
        print('NO')