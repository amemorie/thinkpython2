def factorial(n):
  if n == 0:
    print("returning 1")
    return 1
  else:
    result = n * factorial(n-1)
    print("result "+str(result))
    return result


n=factorial(0)

m=factorial(5)

print(str(m))
