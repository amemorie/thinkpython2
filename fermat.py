
#Fermat's last Theorem says that there are no positive integers a,b,c such that
# a^n + b^n = c^n
# for any values of n greater than 2

def check_fermat(a,b,c,n):
    if n<=2:
        print("Error: Please input a value of n greater than 2")
    #If n is greater than 2 and a^n+b^n=c^n then
    if (a^n)+(b^n)==c^n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")

a=int(input('Please input an integer that will be assigned to value a\n'))
b=int(input('Please input an integer that will be assigned to value b\n'))
c=int(input('Please input an integer that will be assigned to value c\n'))
n=int(input('Please input an integer that will be assigned to value n\n'))

check_fermat(a,b,c,n)
