# Уровень заполненности массива - top

a = [0]*100
top = int(input())
x = True
while x:
    x = int(input())
    a[top] = x
    top += 1
print(a)

