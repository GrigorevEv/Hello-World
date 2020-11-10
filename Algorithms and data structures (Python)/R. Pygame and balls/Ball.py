import pygame

pygame.init()

width = 500
height = 500
radius = 30
pos = []
speed = []

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()


def balls_draw(colour: tuple, xpos, ypos, r):
    """This function draws the ball"""
    ball = pygame.draw.circle(screen, colour, (int(xpos), int(ypos)), r)
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
                speed.append([100, 120])
    return pos, speed


def bounce_off_the_walls(xpos, ypos, x_speed, y_speed, window_width, window_height, r):
    """This function added bounce of the walls"""
    if xpos >= window_width - r or xpos <= 0 + r:
        x_speed = -x_speed
    elif ypos >= window_height - r or ypos <= 0 + r:
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


def wintage(x_speed, y_speed, windage=0.1):
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


def collision(ball1_x, ball1_y, ball2_x, ball2_y):
    """This function added collision of the balls"""
    dist = ((ball1_x - ball2_x)**2 + (ball1_y - ball2_y)**2)**0.5
    if dist <= 30*2:
        return True
    else:
        return False


def colour_change(x_speed):
    """This function changes color of the balls,
    depending on the speed"""
    r = abs(x_speed) * 2

    rgb = (r, 0, 70)
    return rgb


while True:
    coords, speed = events()
    screen.fill((10, 80, 30))

    for i in range(len(coords)):
        x = coords[i][0]
        y = coords[i][1]
        vx = speed[i][0]
        vy = speed[i][1]

        vx, vy = wintage(vx, vy)
        colour = colour_change(abs(vx))
        vx, vy = direction_change(x, y, vx, vy, width, height)
        vx, vy = bounce_off_the_walls(x, y, vx, vy, width, height, radius)

        # for j in range(len(coords)-1, i, -1):
        #     if collision(vx, vy, speed[j][0], speed[j][1]):
        #         vx = speed[j][0]
        #         vy = speed[j][1]
        #         speed[j][0] = -speed[j][0]
        #         speed[j][1] = -speed[j][1]

        x, y = ball_move(x, y, vx, vy)
        balls_draw(colour, x, y, radius)

        coords[i][0] = x
        coords[i][1] = y
        speed[i][0] = vx
        speed[i][1] = vy

    pygame.display.flip()
    pygame.event.pump()

