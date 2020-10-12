# Даны координаты точки и радиус круга с центром в начале координат. Определить, принадлежит ли данная точка кругу.
# Напомним, что круг – это часть плоскости, состоящая из всех точек окружности и всех точек, лежащих внутри окружности.
# Формат входных данных
# Три целых числа на одной строке: координата точки по оси x, координата точки по оси y, радиус круга r (r > 0).
# Формат выходных данных
# Вывести "YES" без кавычек, если точка принадлежит кругу, "NO" без кавычек в противном случае.

x, y, r = map(int, input().split(' '))

c = (x**2 + y**2)**0.5

if c <= r:
    print('YES')
else:
    print('NO')


