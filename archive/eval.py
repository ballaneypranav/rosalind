n = int(input())
s = str(input())
A = [float(x) for x in input().split()]

for a in A:
    p = 1
    for base in s:
        if base in ['A', 'T']:
            p *= (1-a)/2
        else:
            p *= a/2
    print(round((n-len(s)+1) * p, 3), end=' ')
