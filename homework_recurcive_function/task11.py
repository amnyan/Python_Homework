# Write a recursive function to find the sum of the digits of a given number.

def sum(N):
    if not N:
        return 0
    
    return (N % 10) + sum(N // 10)

print(sum(1000000000000000000000000002))