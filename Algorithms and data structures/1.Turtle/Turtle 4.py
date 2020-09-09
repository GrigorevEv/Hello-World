import turtle
import math

turtle.shape('turtle')
x=1
n=500
fi=5
dfi=5
a=10
k=1
while x!=n:


    p=k*(fi+dfi)
    dh=p*dfi
    dp=k*dfi
    turtle.left(fi + dfi)
    turtle.forward((dh**2+dp**2)**0.5)
    x+=1
    fi+=5



