a = (1, 2, 3)
print(a.__sizeof__())
b = list(a)
print(b.__sizeof__())
c = set(a)
print(c.__sizeof__())
a = tuple(c)
print(a.__sizeof__())
b = list(c)
print(b.__sizeof__())