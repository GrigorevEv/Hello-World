# Сдать решение задачи F-Белый король
# На шахматной доске стоят белый король и черный конь.
# Конь неподвижен, король может ходить на одну клетку вправо, на одну клетку вверх или наискосок вправо-вверх.
# Посчитайте, сколькими способами король может дойти до клетки h8, начав с клетки a1.
# Королю нельзя попадать под атаку коня.
# Самого коня есть тоже нельзя.
# Строки шахматной доски пронумерованы числами от 1 до 8, столбцы буквами от a до h.
# Строка 1 - самая нижняя, столбец a - самый левый.
# Формат входных данных
# В единственной строке - позиция коня.
# Позиция - это два символа, буква столбца и номер строки, например a3.
# Формат выходных данных
# Одно число — результат.


def king_horse():
    h = input()
    f = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
    d = [[0] * 12 for i in range(12)]
    ci = 10 - int(h[1])
    cj = 0
    for j in range(8):
        if h[0] == f[j]:
            cj = j + 2
    d[ci][cj] = 4
    for di, dj in moves:
        i = ci + di
        j = cj + dj
        if 1 < i < 10 and 1 < j < 10:
            d[i][j] = 4
    d[10][1] = 1
    for i in range(9, 1, -1):
        for j in range(2, 10):
            if d[i][j] != 4:
                d[i][j] = d[i + 1][j] + d[i][j - 1] + d[i + 1][j - 1]
            else:
                d[i][j] = 0

    for i in range(12):
        print(d[i])
    print(d[2][9])


king_horse()
