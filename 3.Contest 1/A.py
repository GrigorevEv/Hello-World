flag = True
while flag == True:
    x = int(input())
    if x > 999 or x < 100:
        print('введите трехзначное число')
    else:
        a = x//100 + (x % 100)//10 + x % 10
        print(a)
        flag = False