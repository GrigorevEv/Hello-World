# Нарисуйте спираль

import turtle
import math

turtle.shape('turtle')

for i in range(200):
    # i / 20 — смещение точки M по лучу r при повороте на угол, равный одному радиану.
    t = i / 20 * math.pi
    x = t * math.cos(t) * 5
    y = t * math.sin(t) * 5
    turtle.goto(x, y)

