import turtle

def draw(t, length, n):
    if n==0:
        return
    angle=50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

bob=turtle.Turtle()
bob.speed(10)
#draw(bob, 10,5)


def koch(t, x):
    if x<3:
        t.fd(x)
        return
    angle=60.
    koch(t,x/3.)
    t.lt(angle)
    koch(t,x/3.)
    t.rt(2*angle)
    koch(t,x/3.)
    t.lt(angle)
    koch(t,x/3.)

def snowflake(t):
    koch(t,300)
    t.rt(120)
    koch(t,300)
    t.rt(120)
    koch(t,300)
    t.rt(120)

snowflake(bob)
turtle.mainloop()
