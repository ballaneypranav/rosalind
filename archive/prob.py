from math import log10

seq = input()

AT_count = 0
GC_count = 0
for base in seq:
    if base in ['A', 'T']:
        AT_count += 1
    elif base in ['G', 'C']:
        GC_count += 1

GC_contents = [float(x) for x in input().split()]

for x in GC_contents:
    p = x / 2
    q = (1-x) / 2

    a = GC_count * log10(p)
    b = AT_count * log10(q)

    print('%.3f' % (a+b), end=' ')

