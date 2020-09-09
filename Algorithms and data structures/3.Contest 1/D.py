N = int(input())
for i in range(1,N+1):
    k = i**2
    if k > N:
        break
    else:
        print(k, end=' ')