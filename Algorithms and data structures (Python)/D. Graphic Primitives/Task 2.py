# Теперь давайте изменим нашу программу так, чтобы она была разделена на логические независимые куски кода — функции.
# Функции — мощный инструмент. Они позволяют организовать программу так,
# чтобы было удобно работать с её отдельными фрагментами по очереди.
# Идея в том, чтобы разделить наш код на независимые друг от друга по смыслу куски и каждому дать имя.


import graphics as gr

window = gr.GraphWin("Task 1", 1700, 800)
window.setBackground("black")


def horizon():
    horizon1 = gr.Rectangle(gr.Point(0, 400), gr.Point(1700, 800))
    horizon1.setFill('blue')
    horizon1.draw(window)


def ship():
    ship1 = gr.Rectangle(gr.Point(700, 500), gr.Point(900, 600))
    ship2 = gr.Rectangle(gr.Point(700, 500), gr.Point(650, 550))
    ship3 = gr.Rectangle(gr.Point(650, 500), gr.Point(625, 525))
    ship4 = gr.Rectangle(gr.Point(900, 500), gr.Point(950, 550))
    ship5 = gr.Rectangle(gr.Point(950, 500), gr.Point(975, 525))
    ship6 = gr.Rectangle(gr.Point(800, 500), gr.Point(820, 450))

    ship1.setFill('brown')
    ship2.setFill('brown')
    ship3.setFill('brown')
    ship4.setFill('brown')
    ship5.setFill('brown')
    ship6.setFill('gray')

    ship1.setOutline('brown')
    ship2.setOutline('brown')
    ship3.setOutline('brown')
    ship4.setOutline('brown')
    ship5.setOutline('brown')
    ship6.setOutline('gray')

    ship1.draw(window)
    ship2.draw(window)
    ship3.draw(window)
    ship4.draw(window)
    ship5.draw(window)
    ship6.draw(window)


def moon():
    moon = gr.Circle(gr.Point(1355, 100), 30)
    moon.setFill('gray')
    moon.draw(window)


def mast():
    mast1 = gr.Polygon(gr.Point(680,450), gr.Point(850,300), gr.Point(850,450))
    mast2 = gr.Polygon(gr.Point(720,350), gr.Point(850,250), gr.Point(850,350))
    mast3 = gr.Polygon(gr.Point(770,280), gr.Point(850,200), gr.Point(850,280))

    mast1.setFill('white')
    mast2.setFill('white')
    mast3.setFill('white')

    mast1.draw(window)
    mast2.draw(window)
    mast3.draw(window)


def star():
    star1 = gr.Circle(gr.Point(150, 180), 3)
    star2 = gr.Circle(gr.Point(350, 50), 3)
    star3 = gr.Circle(gr.Point(600, 250), 3)
    star4 = gr.Circle(gr.Point(850, 100), 3)
    star5 = gr.Circle(gr.Point(1200, 300), 3)
    star6 = gr.Circle(gr.Point(1600, 180), 3)

    star1.setFill('white')
    star2.setFill('white')
    star3.setFill('white')
    star4.setFill('white')
    star5.setFill('white')
    star6.setFill('white')

    star1.draw(window)
    star2.draw(window)
    star3.draw(window)
    star4.draw(window)
    star5.draw(window)
    star6.draw(window)


def waves():
    waves1 = gr.Line(gr.Point(20, 700), gr.Point(80, 700))
    waves2 = gr.Line(gr.Point(300, 500), gr.Point(360, 500))
    waves3 = gr.Line(gr.Point(550, 650), gr.Point(610, 650))
    waves4 = gr.Line(gr.Point(950, 750), gr.Point(1010, 750))
    waves5 = gr.Line(gr.Point(1250, 550), gr.Point(1310, 550))

    waves1.setFill('gray')
    waves2.setFill('gray')
    waves3.setFill('gray')
    waves4.setFill('gray')
    waves5.setFill('gray')

    waves1.draw(window)
    waves2.draw(window)
    waves3.draw(window)
    waves4.draw(window)
    waves5.draw(window)


def picture():
    horizon()
    ship()
    moon()
    mast()
    star()
    waves()


picture()
window.getMouse()
window.close()
