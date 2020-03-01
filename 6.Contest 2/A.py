x, y, R = map(int, input().split())
S = -R
A = [0]*R*2+[0]

for k in range(len(A)):
    A[k] = S
    S += 1

if x and y in A:
    print('YES')
else:
    print('NO')




