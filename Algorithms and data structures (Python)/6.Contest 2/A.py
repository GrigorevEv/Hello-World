import math
x, y, R = map(int, input().split())

c = math.sqrt(x**2 + y**2)

if c <= R:
    print('YES')
else:
    print('NO')
