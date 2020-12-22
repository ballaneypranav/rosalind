from Bio import SeqIO

def main():
    sequences = []
    for record in SeqIO.parse('rosalind_sseq.txt', "fasta"):
        sequences.append(str(record.seq))

    sequence = sequences[0]
    subsequence = sequences[1]

    i = 0
    j = 0
    while(i < len(sequence) and j < len(subsequence)):
        if sequence[i] == subsequence[j]:
            print(i + 1, end=" ")
            j += 1
        i += 1


if __name__ == "__main__":
    main()



