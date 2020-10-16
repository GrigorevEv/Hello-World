# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import copy


# Извлекаем текст en_ru словаря по url адресу и добавляем его в словарь
url_en_ru = "http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task7/en-ru.txt"
html_en_ru = urllib.request.urlopen(url_en_ru).read()
soup_en_ru = BeautifulSoup(html_en_ru, features="lxml")
text_en_ru = soup_en_ru.get_text()
text_en_ru = text_en_ru[:-1]
en_ru = dict([i.strip() for i in kv.split('\t-\t')] for kv in text_en_ru.split("\n"))

file_en_ru = open('en_ru.txt', 'w')
file_en_ru.write(text_en_ru)
file_en_ru.close()

# Извлекаем текст ru_en словаря по url адресу и добавляем его в словарь
url_ru_en = "http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task7/ru-en.txt"
html_ru_en = urllib.request.urlopen(url_ru_en).read()
soup_ru_en = BeautifulSoup(html_ru_en, features="lxml")
text_ru_en = soup_ru_en.get_text()
text_ru_en = text_ru_en[:-1]
ru_en = dict([i.strip() for i in kv.split('\t-\t')] for kv in text_ru_en.split("\n"))

# Создаем копии, актуализируем их и записываем в текстовые файлы
en_ru_act = en_ru.copy()
ru_en_act = ru_en.copy()

for key_en_ru_act in en_ru:
    for key_ru_en in ru_en:
        if key_en_ru_act == ru_en[key_ru_en]:
            en_ru_act[key_en_ru_act] = en_ru_act[key_en_ru_act] + ', ' + key_ru_en

for key_en_ru in en_ru:
    if en_ru[key_en_ru] not in ru_en:
        ru_en_act[en_ru[key_en_ru]] = key_en_ru

file_en_ru = open('en_ru.txt', 'w')
for key in en_ru_act:
    file_en_ru.write(key + ' - ' + en_ru_act[key] + '\n')
file_en_ru.close()

file_ru_en = open('ru_en.txt', 'w')
for key in ru_en_act:
    file_ru_en.write(key + ' - ' + ru_en_act[key] + '\n')
file_ru_en.close()

