"""Think Python 2nd Ed
by Allen Downey
Chapter 4 Examples 3
"""
import math
import turtle

def pie(t,n,r):
    """Draws a pie divided into radial segments.
    t: turtle
    n: number of segments
    r: length of the radial spokes
    """

    angle=360.0/n
    for f in range(n):
        piesegment(t,r,angle/2.)
        t.lt(angle)

    t.pu()
    t.fd(r*2+10)
    t.pd()

def piesegment(t,r,angle):
    """Draws an isosceles triangle.
    The turtle starts and ends at the peak, facing the middle of the base

    t: turtle
    r: length of the equal legs
    angle: half peak angle in degrees
    """

    y=r*math.sin(angle*math.pi/180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

bob = turtle.Turtle()

# draw a sequence of three pies, as shown in the book.
bob.pu()
bob.bk(130)
bob.pd()
pie(bob, 5, 100)
pie(bob, 6, 100)
pie(bob, 7, 100)

#bob.hideturtle()
turtle.mainloop()
