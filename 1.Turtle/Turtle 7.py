import turtle



def infinity(k,d):
    '''Функция для рисования лепестков.
    k - количество парных лепестков
    d - условный размер лепестка'''
    turtle.shape('turtle')
    turtle.speed(500)
    turtle.left(90)
    n=50
    e=5
    for i in range(k):
        for i in range(n):
            turtle.forward(e)
            turtle.left(360/n)
        for i in range(n):
            turtle.forward(e)
            turtle.right(360/n)
        e+=d
infinity(40,1)
