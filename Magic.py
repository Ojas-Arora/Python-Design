from turtle  import *
import colorsys
bgcolor('black')
title("OJAS")
setup(width=600, height=670)
t=Turtle()

m=0.7


tracer(100)

for i in range(3000):
    c=colorsys.hsv_to_rgb(m,1, 0.99)
    m +=0.002
    t.pencolor(c)
    t.rt(90)
    t.circle(i,m)
    t.lt(180)
    t.fd(m)
    t.rt(170)
    t.fd(m)
    t.rt(90)
    
done()
