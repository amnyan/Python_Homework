#  Write a recursive function to generate the Nth Fibonacci number.

def fib(N):
    if N <= 0:
        return 0
    elif N == 1:
        return 1
    
    return fib(N - 1) + fib(N - 2)

print(fib(6))