# Разложение числа на множители

def factorize_number(x):
    """Раскладывает число на множители.
    Печатает их на экран.
    x - целое положительное число.
    """
    divizor = 2
    while x > 1:
        if x % divizor == 0:
            print(divizor)
            x //= divizor
        else:
            divizor += 1

factorize_number(6544465444)