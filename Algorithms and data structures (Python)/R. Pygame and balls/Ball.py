import sys
import pygame

pygame.init()  # Initialize all imported pygame modules

width = 500
height = 500

screen = pygame.display.set_mode((width, height))  # Initialize a window or screen for display
pygame.display.set_caption('YAHOOOO')  # Returns the title and icontitle for the display Surface. These will often be the same value
clock = pygame.time.Clock()  # Create an object to help track time

x = 30
y = 30
vx = 50
vy = 30

while True:
    dt = clock.tick(50)/300  # The program will never run at more than 50 frames per second

    # for event in pygame.event.get():  # Get events from the queue
    #     if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:  # If user press X or KEYDOWN - program stoped
    #         sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        vx = abs(vx)
    elif key[pygame.K_LEFT]:
        vx = -abs(vx)
    elif key[pygame.K_DOWN]:
        vy = abs(vy)
    elif key[pygame.K_UP]:
        vy = -abs(vy)

    x += vx * dt
    y += vy * dt
    if x >= width or x <= 0:
        vx = -vx
    elif y >= height or y <= 0:
        vy = -vy

    screen.fill((10, 50, 30))
    pygame.draw.circle(screen, (200, 100, 50), (int(x), int(y)), 20, 6)

    pygame.display.flip()  # refreshes the screen and displays everything
    pygame.event.pump()
