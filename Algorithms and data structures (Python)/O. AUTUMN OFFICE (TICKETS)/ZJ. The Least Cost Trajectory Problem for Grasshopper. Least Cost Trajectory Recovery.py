# Задача о траектории наименьшей стоимости для Кузнечика. Восстановление траектории наименьшей стоимости

# Напишите функцию calculate_min_cost(n, price) вычисления наименьшей стоимость достижения клетки n из клетки 1
# Пусть кузнечик прыгает на одну или две точки вперед, а за прыжок в каждую точку
# необходимо заплатить определенную стоимость, различную для различных точек.
# Стоимость прыжка в точку i задается значением price[i] списка price.
# Необходимо найти минимальную стоимость маршрута кузнечика из точки 0 в точку n.
# На этот раз нам необходимо модифицировать определение целевой функции.
# Пусть C[n] — минимальная стоимость пути из 1 в n.
# Выведем рекуррентное соотношение для этой функции.
# Чтобы попасть в точку n мы должны попасть в неё последним прыжком из (n-1) или (n-2).
# Минимальные стоимости этих маршрутов будут равны С[n-1] и С[n-2] соответственно,
# к ним придется добавить значение price[n] за прыжок в клетку n.
# Но из двух клеток мы можем выбрать любую.
# Нужно выбрать тот маршрут, который имеет наименьшую стоимость: C[n] = min(C[n-1], C[n-2]) + price[n]
# Вычислить значение целевой функции также лучше при помощи динамического программирования, а не рекурсии.


def count_min_cost(n, price: list):
    c = [0, price[1], price[2]]+[0]*(n-2)
    for i in range(3, n+1):
        c[i] = price[i] + min(c[i-1], c[i-2])
    print(c[n])


count_min_cost(5, [0, 311, 2, 20, 21, 10])


# Модифицируйте алгоритм вычисления значений целевой функции так,
# чтобы вычислить значения prev[i], и восстановите траекторию наименьшей стоимости из точки 1 в точку n.

def count_min_cost_traj(n, price: list):
    c = [0, price[1], price[2]]+[0]*(n-2)
    for i in range(3, n+1):
        c[i] = price[i] + min(c[i-1], c[i-2])
    prev = [n]
    i = n
    while i > 0:
        if c[i - 1] < c[i - 2]:
            i -= 1
        else:
            i -= 2
        prev.append(i)
    print(c[n])
    print(prev[::-1])


count_min_cost_traj(11, [0, 2, 1, 20, 21, 10, 31, 17, 5, 16, 2, 25])

