import turtle
import math

def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * (abs(angle) / 360)
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)

def draw_a(t,size):
    r=size/2.0
    l=290
    m=360-l
    h=r*math.sin((m/2.)*math.pi/180)
    i=r-h
    t.pu()
    t.lt(90)
    t.fd(size-i)
    t.rt(90)
    t.fd(size)
    t.lt(90+(m/2.))
    t.pd()
    arc(t,r,l)
    t.lt(m/2.)
    t.pu()
    t.fd(size-i)
    t.pd()
    t.rt(180)
    t.fd(size)

    t.pu()
    t.lt(90)
    t.fd(0.3*size)
    t.pd()

def draw_b(t,size):
    r=size/2.
    l=-290
    m=360-abs(l)
    h=(size/2.)*math.sin((m/2.)*math.pi/180)
    i=r-h

    t.pu()
    t.lt(90)
    t.fd(size-i)
    t.rt(m/2.)
    t.pd()
    arc(t,r,l)
    t.rt(m/2.)
    t.pu()
    t.fd((2*size)-i)
    t.pd()
    t.rt(180)
    t.fd(2*size)

    t.pu()
    t.lt(90)
    t.fd((size-i)+0.3*size)
    t.pd()

def draw_c(t,size):
    r=size/2.0
    l=290
    m=360-l
    h=(size/2.)*math.sin((m/2.)*math.pi/180)
    i=r-h

    t.pu()
    t.lt(90)
    t.fd(size-i)
    t.rt(90)
    t.fd(size)
    t.lt(90+(m/2.))
    t.pd()

    arc(t,r,l)
    t.lt(m/2.)
    t.rt(180)

    t.pu()
    t.lt(90)
    t.fd(0.3*size)
    t.lt(90)
    t.bk(i)
    t.rt(90)
    t.pd()

def draw_o(t,size):
    t.pu()
    t.lt(90)
    t.fd(0.5*size)
    t.pd()
    arc(t,size/2.,-360)
    t.pu()
    t.bk(0.5*size)
    t.rt(90)
    t.fd(size+(0.3*size))
    t.pd()


if __name__ == '__main__':

    # create and position the turtle
    bob=turtle.Turtle()
    bob.lt(90)

    fontsize=60
    draw_a(bob,fontsize)
    draw_b(bob,fontsize)
    draw_c(bob,fontsize)
    draw_o(bob,fontsize)
    turtle.mainloop()
