from Bio import SeqIO

def main():
    sequence = ""
    for record in SeqIO.parse('rosalind_revp.txt', "fasta"):
        sequence = str(record.seq)

    for i in range(len(sequence)):
        for j in range(4, 13):
            if i + j <= len(sequence):
                seq = sequence[i:i+j]
                if(seq == reverse_complement(seq)):
                    print(i+1, j)

def reverse_complement(seq):
    result = ""
    for base in seq[::-1]:
        if base == 'A':
            result += 'T'
        elif base == 'T':
            result += 'A'
        elif base == 'C':
            result += 'G'
        elif base == 'G':
            result += 'C'
    return result

if __name__ == "__main__":
    main()