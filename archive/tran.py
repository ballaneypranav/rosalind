from Bio import SeqIO


def main():
    sequences = []
    for record in SeqIO.parse('rosalind_tran.txt', "fasta"):
        sequences.append(str(record.seq))

    transitions = [('A', 'G'), ('G', 'A'),
                   ('C', 'T'), ('T', 'C')]
    transversions = [('A', 'C'), ('A', 'T'),
                     ('G', 'C'), ('G', 'T'),
                     ('C', 'A'), ('C', 'G'),
                     ('T', 'A'), ('T', 'G')]

    transition_count = 0
    transversion_count = 0

    for i in range(len(sequences[0])):
        if   (sequences[0][i], sequences[1][i]) in transitions:
            transition_count += 1
        elif (sequences[0][i], sequences[1][i]) in transversions:
            transversion_count += 1

    print("%.11f" % (transition_count/transversion_count))

if __name__ == "__main__":
    main()