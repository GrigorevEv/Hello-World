l, m, r = [1, 4], [2], [3]
a = l + m + r
print(a)
k = 0
b = [0]*10
for i in l + m + r:
    b[k] = i
    k += 1
print(b)
