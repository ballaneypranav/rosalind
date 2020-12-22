def factorial(n): 
    if n == 1:
        return n
    
    return n * factorial(n-1)

n, r = tuple([int(x) for x in input().split()])

print(int((factorial(n) / factorial(n-r)) % 1000000))