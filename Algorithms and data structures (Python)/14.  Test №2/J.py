# J-Самая вкусная задача
# Перевести число, записанное римскими цифрами, в число, записанное арабскими цифрами.
# Символы: I - 1, V - 5, X - 10, L - 50, C - 100, D - 500, M - 1000
# Выжимка из википедии:
# Натуральные числа записываются при помощи повторения этих цифр.
# При этом, если большая цифра стоит перед меньшей, то они складываются (принцип сложения),
# если же меньшая стоит перед большей, то меньшая вычитается из большей (принцип вычитания).
# Последнее правило применяется только во избежание четырёхкратного повторения одной и той же цифры.
# Формат входных данных
# Строка, представляющая число из римских цифр.
# Формат выходных данных
# Это же число в арабских цифрах. Стоит выводить число, конвертированное в строку, т.е. str(answer)


dig = input()
a = [0]
for symbol in dig:
    if symbol == 'I':
        a.append(1)
    elif symbol == 'V':
        a.append(5)
    elif symbol == 'X':
        a.append(10)
    elif symbol == 'L':
        a.append(50)
    elif symbol == 'C':
        a.append(100)
    elif symbol == 'D':
        a.append(500)
    elif symbol == 'M':
        a.append(1000)

arabic_digit = 0
flag = True
temp = 0
for i in range(len(a)-1, 0, -1):
    if flag is False:
        flag = True
        continue
    if a[i] > a[i-1]:
        arabic_digit += a[i] - a[i-1]
        flag = False
    elif a[i] < a[i-1]:
        arabic_digit += a[i] + a[i-1]
        flag = False
    if a[i] == a[i-1]:
        arabic_digit += a[i]

print(str(arabic_digit))


