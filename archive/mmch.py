from Bio import SeqIO

f = {0: 1, 1: 1}

def main():
    sequence = ""
    for record in SeqIO.parse('rosalind_mmch.txt', "fasta"):
        sequence = str(record.seq)

    A, C, G, U = counts(sequence)

    AU_pairs = nPr(max(A, U), min(A, U))
    GC_pairs = nPr(max(C, G), min(C, G))

    print(int(AU_pairs * GC_pairs))


def counts(seq):
    c = {
        'A': 0,
        'C': 0,
        'G': 0,
        'U': 0
    }

    for base in seq:
        c[base] += 1

    return tuple(c.values())


def nPr(n, r):
    return factorial(n) // factorial(n-r)


def factorial(n):
    if n in f.keys():
        return f[n]
    else:
        f[n] = n * factorial(n-1)
        return f[n]


if __name__ == "__main__":
    main()
