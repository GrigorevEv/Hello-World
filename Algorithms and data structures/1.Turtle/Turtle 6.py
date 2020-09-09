import turtle



def flower(k,s):
    '''Функция для рисования лепестков.
    k - количество парных лепестков
    s - условный размер лепестка'''
    turtle.shape('turtle')
    turtle.speed(500)
    n=100
    for i in range(k):
        for i in range(n):
            turtle.forward(s)
            turtle.left(360/n)
        for i in range(n):
            turtle.forward(s)
            turtle.right(360/n)
        turtle.right(-360/k)
flower(40,7)
