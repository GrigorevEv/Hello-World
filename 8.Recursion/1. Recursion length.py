import sys

def fac(n):
    i = 0
    print(i)
    i += 1
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

fac(50)
# limit = sys.getrecursionlimit()
# # print(limit)