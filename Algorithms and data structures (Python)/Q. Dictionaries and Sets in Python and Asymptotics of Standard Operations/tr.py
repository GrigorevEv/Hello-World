a = [(1, 2), (3, 4), (5, 6)]
for i in range(len(a)):
    x = a[i][0]
    y = a[i][1]
    print('x = ', x, '  ', 'y = ', y, end='\n')
b = [1, 2, 3]
b[0] += 1
print(b)