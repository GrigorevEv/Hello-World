# coding=utf-8
import copy

en_ru = {'home': 'домашняя папка', 'mouse': 'манипулятор мышь'}
ru_en = {'дом': 'home', 'мышь': 'mouse'}
en_ru_act = en_ru.copy()
ru_en_act = ru_en.copy()

for key_en_ru_act in en_ru:
    for key_ru_en in ru_en:
        if key_en_ru_act == ru_en[key_ru_en]:
            en_ru_act[key_en_ru_act] = en_ru_act[key_en_ru_act] + ', ' + key_ru_en

for key_en_ru in en_ru:
    if en_ru[key_en_ru] not in ru_en:
        ru_en_act[en_ru[key_en_ru]] = key_en_ru
print(en_ru)
print(ru_en)
print(en_ru_act)
print(ru_en_act)
