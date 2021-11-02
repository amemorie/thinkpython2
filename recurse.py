#stack diagram for the following program
def recurse(n,s):
    """Recursively adds like a fibonacci sequence"""

    if n==0:
        print(s)
    else:
        recurse(n-1,n+s)

recurse(3,0)

# stack 1: n=3, s=0 so recurse(2,3)
# stack 2: n=2, s=3 so recurse(1,5)
# stack 3: n=1, s=5 so recurse(0,6)
# stack 4: n=0, so print 6

# recurse(-1,0) would continue to stack limit(999)
# stack 1: n=-1, s=0 so recurse(-2,-1)
# stack 2: n=-2, s=-1 so recurse(-3,-3)
# stack 3: n=-3, s=-6 so recurse(-4,-6)

#
