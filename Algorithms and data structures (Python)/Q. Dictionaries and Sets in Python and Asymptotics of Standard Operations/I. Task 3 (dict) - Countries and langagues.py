import urllib.request
from bs4 import BeautifulSoup


# Извлекаем текст словаря по url адресу и добавляем его в словарь
url_dictionary = "http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task5/input.txt"
html_dictionary = urllib.request.urlopen(url_dictionary).read()
soup_dictionary = BeautifulSoup(html_dictionary, features="lxml")
text_dictionary = soup_dictionary.get_text()
text_dictionary = text_dictionary[:-1]
dictionary = dict([i for i in kv.split(' : ')] for kv in text_dictionary.split("\n"))

num_of_lang = int(input())
lang = [input() for i in range(num_of_lang)]

k = 0
for i in range(num_of_lang):
    for key in dictionary:
        if lang[i] in dictionary[key].split():
            if i != k:
                print()
                k = i
            print(key, end=' ')
