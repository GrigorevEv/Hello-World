# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup


# Извлекаем текст словаря по url адресу и добавляем его в словарь
url_dictionary = "http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task6/en-ru.txt"
html_dictionary = urllib.request.urlopen(url_dictionary).read()
soup_dictionary = BeautifulSoup(html_dictionary, features="lxml")
text_dictionary = soup_dictionary.get_text()
text_dictionary = text_dictionary[:-1]
dictionary = dict([i.strip() for i in kv.split('\t-\t')] for kv in text_dictionary.split("\n"))

# Создаем русско-английский словарь
rus_eng = dict()
for key in dictionary:
    rus_eng[dictionary[key]] = key

# Преобразуем словарь в список (для сортировки по ключам) и записываем его в файл
file = open('rus-eng.txt', 'w')
rus_eng_list = list(rus_eng.keys())
rus_eng_list.sort()
for i in rus_eng_list:
    file.write(i + ' - ' + rus_eng[i] + '\n')
