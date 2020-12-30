def main():
    n = int(input())
    A = return_set(input())
    B = return_set(input())

    union = set()
    intersection = set()
    diff_A_B = set()
    diff_B_A = set()
    A_complement = set([x for x in range(1, n+1)])
    B_complement = set([x for x in range(1, n+1)])

    for a in A:
        union.add(a)
        if a in B:
            intersection.add(a)
        else:
            diff_A_B.add(a)
        A_complement.remove(a)
    for b in B:
        union.add(b)
        if b not in A:
            diff_B_A.add(b)
        B_complement.remove(b)
        
    print(union)
    print(intersection)
    print(diff_A_B)
    print(diff_B_A)
    print(A_complement)
    print(B_complement)

def return_set(string):
    return set([int(x) for x in string[1:-1].split(',')])

main()