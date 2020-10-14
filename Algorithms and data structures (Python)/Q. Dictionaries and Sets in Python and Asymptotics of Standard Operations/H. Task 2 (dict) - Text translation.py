import urllib.request
from bs4 import BeautifulSoup

# Извлекаем текст словаря по url адресу и добавляем его в словарь
url_dictionary = "http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task4/en-ru.txt"
html_dictionary = urllib.request.urlopen(url_dictionary).read()
soup_dictionary = BeautifulSoup(html_dictionary, features="lxml")
text_dictionary = soup_dictionary.get_text()
text_dictionary = text_dictionary[:-1]
dictionary = dict([i.strip() for i in kv.split('\t-\t')] for kv in text_dictionary.split("\n"))

# Извлекаем текст для перевода по url адресу
url_to_translate = "http://judge.mipt.ru/mipt_cs_on_python3/extra/lab17/task4/input.txt"
html_to_translate = urllib.request.urlopen(url_to_translate).read()
soup_to_translate = BeautifulSoup(html_to_translate, features="lxml")
text_to_translate = soup_to_translate.get_text()

print(text_to_translate)

