# think python 2

# ackerman function
# A(m,n) = { n+1                if m=0
#            A(m-1,1)           if m>0 and n=0
#            A(m-1, A(m,n-1))   if m>0 and n>0

def ack(m,n):
    if m == 0:
        a = n + 1
        return a
    if n == 0:
        return ack(m-1, 1)
    return ack(m-1, ack(m, n-1))
        
a = ack(3, 4)
print(str(a))
