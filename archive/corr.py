
from codecs import IncrementalDecoder
from Bio import SeqIO

def main():
    sequences = []
    for record in SeqIO.parse('rosalind_corr.txt', "fasta"):
        sequences.append(str(record.seq))

    counts = {}
    for seq in sequences:
        if seq not in counts.keys():
            counts[seq] = 1
        else:
            counts[seq] += 1

    correct = []
    incorrect = []
    
    for seq in counts.keys():
        revc = reverse_complement(seq)
        if revc in counts.keys():
            if counts[seq] + counts[revc] > 1:
                if seq not in correct and revc not in correct:
                    correct.append(seq)
        elif counts[seq] > 1:
            correct.append(seq)
        else:
            incorrect.append(seq)

    for i_seq in incorrect:
        for c_seq in correct:
            revc = reverse_complement(c_seq)
            if hamming(i_seq, c_seq) == 1:
                print(i_seq + "->" + c_seq)
                break
            elif hamming(i_seq, revc) == 1:
                print(i_seq + "->" + revc)
                break


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

def hamming(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

if __name__ == "__main__":
    main()