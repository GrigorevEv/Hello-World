import sys

i = 0


def fac(n):
    global i
    i += 1
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

print(fac(997))
print(i)
print(sys.getrecursionlimit())
