from Bio import SeqIO

def main():
    seq = ""
    for record in SeqIO.parse('rosalind_kmp.txt', "fasta"):
        seq = str(record.seq)

    p = [0]

    # seq[j:k] = s[1:k-j+1]

    i = 0
    for j in range(1, len(seq)):
        p.append(0)
        while seq[i] != seq[j] and i > 0:
            i -= 1
            i = p[i]
        if seq[i] == seq[j]:
            p[j] = i+1
            i += 1
    print(*p)

main()
