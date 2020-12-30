
from Bio import SeqIO


def main():
    sequence = ''
    for record in SeqIO.parse('rosalind_motz.txt', "fasta"):
        sequence = str(record.seq)

    print(NCM(sequence))

dic = {}
def NCM(seq):

    if seq in dic.keys():
        return dic[seq]
    elif len(seq) in [0, 1]:
        return 1

    count = NCM(seq[1:])
    matches = [('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G')]
    for i in range(1, len(seq)):
        if (seq[0], seq[i]) in matches:
            count += NCM(seq[1:i]) * NCM(seq[i+1:])
            
    dic[seq] = count
    return count % 1000000


def counts_match(seq):
    counts = {'A': 0, 'U': 0, 'G': 0, 'C': 0}
    for base in seq:
        counts[base] += 1

    return counts['A'] == counts['U'] and counts['G'] == counts['C']


if __name__ == "__main__":
    main()
