import turtle

turtle.shape('turtle')
n=12
for i in range(12):
    turtle.right(360/n)
    turtle.forward(100)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(100)
    turtle.right(180)


