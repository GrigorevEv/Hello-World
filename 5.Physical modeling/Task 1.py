import graphics as gr

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
rectangle.setFill('#8FBC8F')
rectangle.draw(window)

coords = gr.Point(200, 200) #  Начальное положение шарика
velocity = gr.Point(1, -2) #  Скорость
acceleration = gr.Point(0, 0.1) #  Ускорение

circle = gr.Circle(gr.Point(200, 200), 10)
circle.setFill('#665D1E')
circle.draw(window)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('#8FBC8F')
    rectangle.draw(window)


def ball_move(point):



def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


while True:
    ball_move(velocity)
    coords = add(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)

    gr.time.sleep(0.02)