import math

# ex 7.1
def mysqrt(a):
    x = a / 2.
    while True:
        y = (x + a / x) / 2.
        epsilon = 0.01
        if abs(y-x) < epsilon:
            return y
        x = y

def test_sqrt():
    print("a    mysqrt(a)      math.sqrt(a)    diff")
    print("---  -------------  --------------- ------------------")
    for j in range(9):
        i = float(j+1)
        a = mysqrt(i)
        b = math.sqrt(i)
        d = a - b
        print(str(i)+" "+str(a)+" "+str(b)+" "+str(d))

#test_sqrt()

#ex 7.2
def eval_loop():
    i = ""
    while True:
        i = input("type in something to evaluate")
        if i == "done":
            print("Done!")
            break
        j = eval(i)
        print(j)

#eval_loop()

def factorial(n):
  if n == 0:
    return 1
  else:
    result = n * factorial(n-1)
    return result


def estimatepi():
    epsilon = 1e-15
    k = 0
    m = ((2*math.sqrt(2))/9801)

    total = 0
    while True:
        n = (factorial(4 * k)*(1103+(26390*k)))/((factorial(k) ** 4) * (396 ** (4 * k)))
        term = m * n
        total += term
        if abs(term) < epsilon:
            break
        k += 1
    
    print(1./total, math.pi)
    return 1./total

estimatepi()
