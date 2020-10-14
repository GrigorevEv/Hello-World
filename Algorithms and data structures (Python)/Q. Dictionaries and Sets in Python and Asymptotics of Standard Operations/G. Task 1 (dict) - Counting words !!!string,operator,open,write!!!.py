import string
import operator

file = open('text1.txt')
formated_txt = open('text2.txt', 'w')
file = file.read()
punctuation = string.punctuation
for index in file:
    if index not in punctuation and index not in '\n':
        formated_txt.write(index.lower())
formated_txt.close()

dictionary = dict()
formated_txt = open('text2.txt')
formated_txt = formated_txt.read()
array = list(map(str, formated_txt.split()))
for key in array:
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
formated_txt = open('text2.txt', 'w')
for a in dictionary:
    print(a[0], ':', a[1])
    formated_txt.write(a[0] + ' : ' + str(a[1]) + '\n')

formated_txt.close()
