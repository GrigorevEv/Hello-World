# Наивный поиск подстроки в строке


def equal(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def search_substring(s, sub):
    for i in range(0, (len(s) - len(sub))):
        if equal(s[i:i + len(sub)], sub):
            print(i)


search_substring('bbccbcbcbabcbccbabcbb', 'abc')

