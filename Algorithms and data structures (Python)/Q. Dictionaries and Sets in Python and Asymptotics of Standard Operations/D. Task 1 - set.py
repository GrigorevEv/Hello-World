# Вывести на экран все элементы множества A, которых нет в множестве B.

A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
print(A, B, sep='\n')
for x in A:
    if x in B:
        print(x, end=' ')

