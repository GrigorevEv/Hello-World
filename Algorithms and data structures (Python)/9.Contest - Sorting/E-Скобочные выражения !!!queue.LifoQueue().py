# Сдать решение задачи E-Скобочные выражения
# Входные данные
# Слово в алфавите из двух круглых скобочек ( и ). Длина слова меньше 4001
# Выходные данные
# Либо NO, либо YES
# https://docs.python.org/3/library/queue.html
# https://www.guru99.com/python-queue-example.html

import queue

q = queue.LifoQueue()
s = input()

for brace in s:
    if brace in '(':
        q.put(brace)
    else:
        if q.empty():
            print('NO')
        left = q.get()
if q.empty():
    print('YES')
else:
    print('NO')


# ------------------------------------------------------
#
#
# s = input()
# meetings = 0
#
# for brace in s:
#     if brace == '(':
#         meetings += 1
#     else:
#         meetings -= 1
#         if meetings < 0:
#             print('NO')
# if meetings == 0:
#     print('YES')
# else:
#     print('NO')
#
#
# ------------------------------------------------------------------
#
#
# s = input()
# while '()' in s:
#     s = s.replace('()', '')
# if not s:
#     print('YES')
# else:
#     print('NO')
