# think python 2
# exercise 6.1
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

#x = 1
#y = x + 1
#print(c(x, y + 3, x + y))

# x = 1
# y = 2
# c(1,5,3)
# stack 1 func c => total = 1 + 5 + 3 = 9
#                   square = (b(9))^2
#                          = 90^2 = 8100
# stack 2 func b => prod = a(9,9)
# stack 3 func a => x = 9+1 = 10
#                => return(90)


# exercise 6.4
def is_power(a, b):
    if a==b:
        return True
    elif a%b ==0:
        return is_power(a/b, b)

    return False


#print(is_power(128, 2))
#print(is_power(3125, 5))
#print(is_power(3120, 5))
#print(is_power(7, 7))
#print(is_power(1, 1))
#print(is_power(0, 0))


# exercise 6.5

def gcd(a,b):
    r = a % b
    print(a,b,r)
    if r != 0:
        return gcd(b,r)
    return b


a = 24
b = 16
c = gcd(a,b)
print(c)
