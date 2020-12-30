from Bio import SeqIO
from sys import setrecursionlimit
setrecursionlimit(2000)

def main():
    sequences = []
    for record in SeqIO.parse('rosalind_edit.txt', "fasta"):
        sequences.append(str(record.seq))

    print(edit_distance(sequences[0], sequences[1]))

calculated_results = {}

def edit_distance(s1, s2):
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)

    if (s1, s2) in calculated_results.keys():
        return calculated_results[(s1, s2)]

    if s1[-1] == s2[-1]:
        result = edit_distance(s1[:-1], s2[:-1])
        calculated_results[(s1, s2)] = result
        return result
    else:
        # insertion
        a = edit_distance(s1, s2[:-1]) + 1
        # deletion
        b = edit_distance(s1[:-1], s2) + 1
        # replace
        c = edit_distance(s1[:-1], s2[:-1]) + 1

        result = min(a, b, c)
        calculated_results[(s1, s2)] = result
        return result

main()