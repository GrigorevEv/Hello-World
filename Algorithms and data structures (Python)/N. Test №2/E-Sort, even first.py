# Сортировка: сначала чётные
# Дан список целых чисел. Отсортировать его так,
# чтобы сначала шли чётные по возрастанию, потом — нечётные во возрастанию.
# Формат входных данных
# Одна строка — список чисел через пробел. Длина списка не превосходит 10000.
# Формат выходных данных
# Отсортированный список чисел через пробел

digits = list(map(int, input().split()))
even_sorted_digits = []
odd_even_sorted_digits = []
sorted_digits = []
digits.sort()
for i in range(len(digits)):
    if digits[i] % 2 == 0:
        even_sorted_digits.append(digits[i])
    else:
        odd_even_sorted_digits.append(digits[i])
sorted_digits = even_sorted_digits + odd_even_sorted_digits
for i in range(len(sorted_digits)):
    print(sorted_digits[i], end=' ')


