# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение наибольшего четного элемента последовательности.
# Числа, следующие за нулем, считывать не нужно.
# Формат входных данных
# Последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
# Каждое число на новой строке.
# Формат выходных данных
# Одно число — максимальное четное число в последовательности, если четные числа в ней присутствуют, иначе - 0.


digit = 0
a = None
while a != 0:
    a = int(input())
    if a == 0:
        break
    if a % 2 == 0 and a > digit:
        digit = a
print(digit)
