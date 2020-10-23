import pygame

pygame.init()  # Initialize all imported pygame modules

width = 500
height = 500

screen = pygame.display.set_mode((width, height))  # Initialize a window or screen for display
pygame.display.set_caption('YAHOOOO')  # Returns the title and icontitle for the display Surface. These will often be the same value
clock = pygame.time.Clock()  # Create an object to help track time

x1, x2, y1, y2 = 30, 470, 30, 470
vx1, vy1, vx2, vy2 = 50, 30, 30, 50
windage = 0.001

while True:
    dt = clock.tick(50)/300  # The program will never run at more than 50 frames per second

    for event in list(pygame.event.get()):  # Get events from the queue
        if event.type == pygame.QUIT:  # If user press X  - program stoped
            raise SystemExit

    # Adding direction change

    if 0 < x1 < width and 0 < y1 < height or 0 < x2 < width and 0 < y2 < height:
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            vx1 = abs(vx1)
            vx2 = abs(vx2)
        elif key[pygame.K_LEFT]:
            vx1 = -abs(vx1)
            vx2 = -abs(vx2)
        elif key[pygame.K_DOWN]:
            vy1 = abs(vy1)
            vy2 = abs(vy2)
        elif key[pygame.K_UP]:
            vy1 = -abs(vy1)
            vy2 = -abs(vy2)

    # Adding windage

    if vx1 != 0 or vy1 != 0 or vx2 != 0 or vy2 != 0:
        if vx1 > 0:
            vx1 -= windage
        else:
            vx1 += windage
        if vy1 > 0:
            vy1 -= windage
        else:
            vy1 += windage
        if vx2 > 0:
            vx2 -= windage
        else:
            vx2 += windage
        if vy2 > 0:
            vy2 -= windage
        else:
            vy2 += windage

    # Adding path

    x1 += vx1 * dt
    y1 += vy1 * dt
    x2 += vx2 * dt
    y2 += vy2 * dt

    # Adding bounce off the walls

    if x1 >= width or x1 <= 0:
        vx1 = -vx1
    elif y1 >= height or y1 <= 0:
        vy1 = -vy1
    if x2 >= width or x2 <= 0:
        vx2 = -vx2
    elif y2 >= height or y2 <= 0:
        vy2 = -vy2

    # Adding colour change

    r = abs(vx1) * 5
    g = abs(vx2) * 5



    # Adding colision of balls


    radius = 20
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if dist <= radius * 2:
        quit()



    screen.fill((10, 50, 30))
    pygame.draw.circle(screen, (r, 70, 70), (int(x1), int(y1)), radius, 9)
    pygame.draw.circle(screen, (70, g, 70), (int(x2), int(y2)), radius, 9)
    pygame.display.flip()  # refreshes the screen and displays everything
    pygame.event.pump()
