def main():
    n, x = input().split()
    n = int(n)
    x = float(x)
    s = input()

    print(seq_prob(n, x, s))

def seq_prob(n, gc_content, seq):
    prob = 1
    for base in seq:
        if base in "GC":
            prob *= gc_content * 0.5
        else:
            prob *= (1 - gc_content) * 0.5
    return 1 - (1 - prob)**n

main()