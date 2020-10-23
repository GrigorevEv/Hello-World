import pygame

pygame.init()  # Initialize all imported pygame modules

width = 500
height = 500
x, y = 30, 30
vx, vy = 50, 60


screen = pygame.display.set_mode((width, height))  # Initialize a window or screen for display
pygame.display.set_caption('YAHOOOO')  # Returns the title and icon title for the display Surface.
clock = pygame.time.Clock()


def balls_draw(colour, xpos=30, ypos=30, radius=20):
    """This function draws the ball"""
    ball1 = pygame.draw.circle(screen, colour, (int(xpos), int(ypos)), radius)
    ball2 = pygame.draw.circle(screen, colour, (int(xpos), int(ypos)), radius)
    return ball1, ball2


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


def wintage(x_speed, y_speed, windage=0.05):
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
    r = abs(x_speed) * 5
    g = abs(y_speed) * 2
    b = abs(y_speed) * 2
    rgb = (r, g, b)
    return rgb


while True:
    for event in list(pygame.event.get()):  # Get events from the queue
        if event.type == pygame.QUIT:  # If user press X  - program stoped
            raise SystemExit

    screen.fill((10, 80, 30))
    vx, vy = wintage(vx, vy)
    vx, vy = direction_change(x, y, vx, vy, width, height)
    vx, vy = bounce_off_the_walls(x, y, vx, vy, width, height)
    colour = colour_change(vx, vy)
    x, y = ball_move(x, y, vx, vy)
    balls_draw(colour, x, y)

    pygame.display.flip()  # refreshes the screen and displays everything
    pygame.event.pump()

