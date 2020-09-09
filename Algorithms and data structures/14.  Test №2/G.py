# Треугольник Паскаля
# По данному числу N выведите первые N+1 строку треугольника Паскаля.
# Формат входных данных
# Во входных данных содержится только число N (0 < N ≤ 100).
# Формат выходных данных
# Выведите N + 1 строку треугольника Паскаля.
# Числа в строке разделяйте одним пробелом.

N = int(input()) + 1
trang = []
for i in range(N):
    temp_list = []
    for j in range(i+1):
        if j == 0 or j == i:
            temp_list.append(1)
        else:
            temp_list.append(trang[i-1][j-1] + trang[i-1][j])
    trang.append(temp_list)
for i in range(N):
    for j in range(i+1):
        print(trang[i][j], end=' ')
    print()    # для вывода с новой строки
