s = int(input())
k = 0
p = 0
while s != 0:
    if s > k:
        k = s
        p = 0
    if s == k:
        p += 1
    s = int(input())
print(p)