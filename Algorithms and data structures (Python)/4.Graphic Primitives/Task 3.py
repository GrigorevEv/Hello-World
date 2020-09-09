import graphics as gr

window = gr.GraphWin("Task 1", 1700, 800)
window.setBackground("black")

def horizon(x1,y1,x2,y2,colour):
    horizon = gr.Rectangle(gr.Point(x1, y1), gr.Point(x2, y2))
    horizon.setFill(colour)
    horizon.draw(window)


def ship(x1,y1,x2,y2,colour1,colour2):
    ship = gr.Rectangle(gr.Point(x1, y1), gr.Point(x2, y2))
    ship.setFill(colour1)
    ship.setOutline(colour2)
    ship.draw(window)


def moon(x,y,size,colour):
    moon = gr.Circle(gr.Point(x, y), size)
    moon.setFill(colour)
    moon.draw(window)


def mast(x1,y1,x2,y2,x3,y3,colour):
    mast = gr.Polygon(gr.Point(x1,y1), gr.Point(x2,y2), gr.Point(x3,y3))
    mast.setFill(colour)
    mast.draw(window)


def star(x,y,size,colour):
    star = gr.Circle(gr.Point(x, y), size)
    star.setFill(colour)
    star.draw(window)


def waves(x1,y1,x2,y2,colour):
    waves = gr.Line(gr.Point(x1, y1), gr.Point(x2, y2))
    waves.setFill(colour)
    waves.draw(window)


def picture():
    horizon(0,400,1700,800,'blue')
    ship(700,500,900,600,'brown','brown')
    ship(700, 500, 650, 550, 'brown', 'brown')
    ship(650, 500, 625, 525, 'brown', 'brown')
    ship(900, 500, 950, 550, 'brown', 'brown')
    ship(950, 500, 975, 525, 'brown', 'brown')
    ship(800, 500, 820, 450, 'gray', 'black')
    moon(1335, 100, 30, 'gray')
    mast(680, 450, 850, 300, 850, 450, 'white')
    mast(720, 350, 850, 250, 850, 350, 'white')
    mast(770, 280, 850, 200, 850, 280, 'white')
    star(150, 180, 3, 'white')
    star(350, 50, 3, 'white')
    star(600, 250, 3, 'white')
    star(850, 100, 3, 'white')
    star(1200, 300, 3, 'white')
    star(1600, 180, 3, 'white')
    waves(20, 700, 80, 700, 'gray')
    waves(300, 500, 360, 500, 'gray')
    waves(550, 650, 610, 650, 'gray')
    waves(950, 750, 1010, 750, 'gray')
    waves(1250, 550, 1310, 550, 'gray')


picture()
window.getMouse()
window.close()
