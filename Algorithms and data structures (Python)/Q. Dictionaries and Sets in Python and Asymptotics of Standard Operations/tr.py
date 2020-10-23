def ab(x, y):
    x = x+5
    y = y+10
    return x, y

x, y = 5, 6

x, y = ab(x, y)

print(x, y)