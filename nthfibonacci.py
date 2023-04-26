def nthFibonacciNumber(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2: 
        return 1
    return nthFibonacciNumber(n-1)+nthFibonacciNumber(n-2)
print(nthFibonacciNumber(10))
