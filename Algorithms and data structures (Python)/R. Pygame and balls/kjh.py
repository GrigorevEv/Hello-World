import pygame

pygame.init()

width = 500
height = 500
x, y = 30, 30
vx, vy = 100, 120
pos = []

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()


def balls_draw(colour: tuple, xpos, ypos, radius=20):
    """This function draws the ball"""
    ball = pygame.draw.circle(screen, colour, (int(xpos), int(ypos)), radius)
    return ball


def events():
    """This function added events and also return coordinates of mouse clicks,
    for generate new balls"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos.append(list(event.pos))
    return pos


def bounce_off_the_walls(xpos, ypos, x_speed, y_speed, window_width, window_height):
    """This function added bounce of the walls"""
    if xpos >= window_width or xpos <= 0:
        x_speed = -x_speed
    elif ypos >= window_height or ypos <= 0:
        y_speed = -y_speed
    return x_speed, y_speed


def direction_change(xpos, ypos, x_speed, y_speed, window_width, window_heigh):
    """This function change direction of the ball"""
    if 0 < xpos < window_width and 0 < ypos < window_heigh or 0 < xpos < window_width and 0 < ypos < window_heigh:
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            x_speed = abs(x_speed)
        elif key[pygame.K_LEFT]:
            x_speed = -abs(x_speed)
        elif key[pygame.K_DOWN]:
            y_speed = abs(y_speed)
        elif key[pygame.K_UP]:
            y_speed = -abs(y_speed)
    return x_speed, y_speed


def wintage(x_speed, y_speed, windage=0.001):
    """This function added windage to the ball's speed"""
    if x_speed != 0 or y_speed != 0 or x_speed != 0 or y_speed != 0:
        if x_speed > 0:
            x_speed -= windage
        else:
            x_speed += windage
        if y_speed > 0:
            y_speed -= windage
        else:
            y_speed += windage
    return x_speed, y_speed


def ball_move(xpos, ypos, x_speed, y_speed):
    """This function move the ball"""
    dt = clock.tick(50)/300
    xpos += x_speed * dt
    ypos += y_speed * dt
    return xpos, ypos


def colour_change(x_speed, y_speed):
    """This function changes color of the balls,
    depending on the speed"""
    r = abs(x_speed) * 2
    g = abs(y_speed) * 2
    b = abs(y_speed) * 2
    rgb = (r, g, b)
    return rgb


while True:
    coords = events()
    screen.fill((10, 80, 30))

    vx, vy = wintage(vx, vy)
    colour = colour_change(vx, vy)
    vx, vy = direction_change(x, y, vx, vy, width, height)
    vx, vy = bounce_off_the_walls(x, y, vx, vy, width, height)

    for i in range(len(coords)):
        x = coords[i][0]
        y = coords[i][1]
        x, y = ball_move(x, y, vx, vy)
        balls_draw(colour, x, y)
        coords[i][0] = x
        coords[i][1] = y

    pygame.display.flip()
    pygame.event.pump()

