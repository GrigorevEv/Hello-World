# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Важная подсказка: в питоне есть функция ord(chr) -> int. Возвращает числовое представление для указанного символа.
# Например, ord('a') вернет 97. Коды идут последовательно, то есть ord('a') = 97, ord('b') = 98 и так далее.
# Формат входных данных
# На вход программе подается одна строка.
# Формат выходных данных
# Два числа - количество прописных и строчных букв. Вывести в одну строку через пробел.

string = input()
new_string =[]
for letter in string:
    if letter in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
        new_string.append(letter)
capital_letter = 0
lowercase_letter = 0
for letter in new_string:
    if ord(letter) <= 90:
        capital_letter += 1
    else:
        lowercase_letter += 1
print(capital_letter, lowercase_letter, end=' ')
