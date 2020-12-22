from Bio import SeqIO

def main():
    sequences = []
    for record in SeqIO.parse('rosalind_pdst.txt', "fasta"):
        sequences.append(str(record.seq))

    matrix = []

    for i in range(len(sequences)):
        matrix.append([])
        for j in range(len(sequences)):
            matrix[i].append(0)
            if j < i:
                matrix[i][j] = matrix[j][i]
                continue
            elif j == i:
                matrix[i][j] = 0
                matrix[j][i] = 0
            else:
                matrix[i][j] = distance(sequences[i], sequences[j])

    for i in matrix:
        for j in i:
            print("%.5f" % j, end=" ")
        print()

def distance(s, t):
    d = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            d += 1
    return d / len(s)

main()