# I-B-функция
# Зафиксируем строку L.
# Будем называть её подстроку K особенной, если у неё есть как минимум три различных вхождения в L,
# среди которых префикс и суффикс строки L.
# Пусть теперь дана строка S, состоящая из N символов.
# Пусть B(i) - длина максимальной особенной подстроки у строки, образованной первыми i символами S.
# Напишите программу, которая вычислит значения функции B
# для заданной строчки для всех возможных значений i от 1 до N (нумерация от 1).
# Формат входных данных
# В единственной строке записана строка, состоящая только из больших и/или маленьких латинских букв.
# Длина строки 1 <= N <= 200000.
# Формат выходных данных
# В выходной файл выведите N чисел — значения функции B(1), B(2), … B(N).
import time
start_time = time.time()

string = "ikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyikizikiyikixikixikixikiyikizikiyikixikiyikixikiyikizikiyikixikizikixikiyikizikiyikixikiyikixikiyik"
string_array = list(string)
B = [0]*len(string)


# 1. Считаем префикс функцию, чтобы узнать длины всех подстрок строки s совпадающих с префиксом этой строки
def p_func(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    return pi


pi = p_func(string)
c = []

# 2. Сравниваем полученные префиксы с отрезками строки, и считаем вхождения.
# Если кол-во вхождений (в том числе и пересекающихся) больше или равно 2 (это означает что в самой строке их
# больше или равно 3, учитывая сам префикс) то B[j+pi[i]-1] = pi[i]
for i in range(len(pi)//2):
    k = 0
    if pi[i] == 0:
        continue
    if pi[i] in c:
        B[i] = pi[i]
        continue
    for j in range(len(string_array)):
        if string_array[j:j+pi[i]] == string_array[0:pi[i]]:
            if k >= 2:
                B[j+pi[i]-1] = pi[i]
                c.append(pi[i])
            else:
                k += 1
for i in range(len(B)):
    print(B[i], end=' ')
print()
print("time elapsed: {:.2f}s".format(time.time() - start_time))