# Используя полученные знания, нарисуйте любую статическую сцену,
# которая содержит не менее 5 различных объектов, состоящих из пяти и более примитивов.
# Проявите свою творческую натуру, но не занимайтесь этим более 30 минут,
# ведь вашу сцену можно улучшать вечно, а наша задача немного в другом.


import graphics as gr

window = gr.GraphWin("Task 1", 1700, 800)
window.setBackground("black")


horizon1 = gr.Rectangle(gr.Point(0, 400), gr.Point(1700, 800))
horizon1.setFill('blue')
horizon1.draw(window)


ship1 = gr.Rectangle(gr.Point(700, 500), gr.Point(900, 600))
ship1.setFill('brown')
ship1.setOutline('brown')
ship1.draw(window)
ship2 = gr.Rectangle(gr.Point(700, 500), gr.Point(650, 550))
ship2.setFill('brown')
ship2.setOutline('brown')
ship2.draw(window)
ship3 = gr.Rectangle(gr.Point(650, 500), gr.Point(625, 525))
ship3.setFill('brown')
ship3.setOutline('brown')
ship3.draw(window)
ship4 = gr.Rectangle(gr.Point(900, 500), gr.Point(950, 550))
ship4.setFill('brown')
ship4.setOutline('brown')
ship4.draw(window)
ship5 = gr.Rectangle(gr.Point(950, 500), gr.Point(975, 525))
ship5.setFill('brown')
ship5.setOutline('brown')
ship5.draw(window)
ship6 = gr.Rectangle(gr.Point(800, 500), gr.Point(820, 450))
ship6.setFill('gray')
ship6.setOutline('gray')
ship6.draw(window)


moon = gr.Circle(gr.Point(1355, 100), 30)
moon.setFill('gray')
moon.draw(window)


mast1 = gr.Polygon(gr.Point(680,450), gr.Point(850,300), gr.Point(850,450))
mast1.setFill('white')
mast1.draw(window)
mast2 = gr.Polygon(gr.Point(720,350), gr.Point(850,250), gr.Point(850,350))
mast2.setFill('white')
mast2.draw(window)
mast3 = gr.Polygon(gr.Point(770,280), gr.Point(850,200), gr.Point(850,280))
mast3.setFill('white')
mast3.draw(window)


star_circle1 = gr.Circle(gr.Point(150, 180), 3)
star_circle1.setFill('white')
star_circle1.draw(window)
star_circle2 = gr.Circle(gr.Point(350, 50), 3)
star_circle2.setFill('white')
star_circle2.draw(window)
star_circle3 = gr.Circle(gr.Point(600, 250), 3)
star_circle3.setFill('white')
star_circle3.draw(window)
star_circle4 = gr.Circle(gr.Point(850, 100), 3)
star_circle4.setFill('white')
star_circle4.draw(window)
star_circle5 = gr.Circle(gr.Point(1200, 300), 3)
star_circle5.setFill('white')
star_circle5.draw(window)
star_circle6 = gr.Circle(gr.Point(1600, 180), 3)
star_circle6.setFill('white')
star_circle6.draw(window)


waves1 = gr.Line(gr.Point(20, 700), gr.Point(80, 700))
waves1.setFill('gray')
waves1.draw(window)
waves2 = gr.Line(gr.Point(300, 500), gr.Point(360, 500))
waves2.setFill('gray')
waves2.draw(window)
waves3 = gr.Line(gr.Point(550, 650), gr.Point(610, 650))
waves3.setFill('gray')
waves3.draw(window)
waves4 = gr.Line(gr.Point(950, 750), gr.Point(1010, 750))
waves4.setFill('gray')
waves4.draw(window)
waves5 = gr.Line(gr.Point(1250, 550), gr.Point(1310, 550))
waves5.setFill('gray')
waves5.draw(window)
waves5 = gr.Line(gr.Point(1550, 650), gr.Point(1610, 650))
waves5.setFill('gray')
waves5.draw(window)


window.getMouse()
window.close()
